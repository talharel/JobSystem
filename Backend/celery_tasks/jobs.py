from celery_worker import celery_app
from finders.comeet_finder import ComeetFinder
from finders.indeed_finder import IndeedFinder
from services.jobs import JobService
from database import get_db
import asyncio
import config_file


async def update_jobs():
    comeet_finder = ComeetFinder('Comeet Finder', config_file.config_app.get('comeet_url'), platform_name='commet')
    indeed_finder = IndeedFinder('Indeed Finder', config_file.config_app.get('indeed_url'), platform_name='indeed')
    async for db in get_db():
        jobService = JobService(db)
        jobService.add_finder(comeet_finder)
        jobService.add_finder(indeed_finder)

        jobs = jobService.get_jobs_from_finders()
        await jobService.update_jobs_in_db(jobs)

    return {'status': 'Task Succeed'}


@celery_app.task(bind=True, acks_late=True)
def celery_task_update_jobs(self):
    try:
        asyncio.run(update_jobs())
    except Exception as e:
        self.retry(countdown=4)
