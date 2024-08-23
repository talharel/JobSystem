from celery_worker import celery_app
from finders.comeet_finder import ComeetFinder
from finders.indeed_finder import IndeedFinder
from services.jobs import JobService
import config_file





@celery_app.task(bind=True, max_retries=4)
def celery_task_update_jobs(self):
    try:
        comeet_finder = ComeetFinder('Comeet Finder', config_file.config_app.get('comeet_url'),platform_name='commet')
        indeed_finder = IndeedFinder('Indeed Finder', config_file.config_app.get('indeed_url'),platform_name='indeed')

        jobService = JobService()
        jobService.add_finder(comeet_finder)
        jobService.add_finder(indeed_finder)

        jobs = jobService.get_jobs_from_finders()
        jobService.update_jobs_in_db(jobs)
        return 'Task Success'
    except Exception as e:
        self.retry(countdown=4)
