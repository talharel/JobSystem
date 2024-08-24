from sqlalchemy.future import select
from sqlalchemy import func
from models.jobs import Job
from finders.comeet_finder import ComeetFinder
from finders.indeed_finder import IndeedFinder
from typing import List
from schemas.jobs import JobDetails
from database import get_db
from schemas.finders import Finder
import asyncio
import config_file


class JobService:

    def __init__(self, db=None):
        self.finders = []
        self.db = db

    def add_finder(self, finder: Finder):
        if not isinstance(finder, Finder):
            raise Exception('Not a Finder Instance')

        self.finders.append(finder)

    def get_jobs_from_finders(self) -> List[JobDetails]:
        jobs = []
        for finder in self.finders:
            try:
                found_jobs = finder.get_jobs_from_platform()
                jobs.extend(found_jobs)
            except Exception as e:
                print(f"Failed to fetch jobs from {finder.finder_name}: {str(e)}")
        return jobs

    async def update_jobs_in_db(self, jobs: list):
        try:

            result = await self.db.execute(select(Job))
            existing_urls = {job.url for job in result.scalars().all()}

            new_jobs = [
                Job(
                    company_name=job.company_name,
                    url=job.job_url,
                    status='not_viewed',
                    platform_name=job.platform_name
                )
                for job in jobs
                if job.job_url not in existing_urls
            ]

            if new_jobs:
                self.db.add_all(new_jobs)
                await self.db.commit()
                print("New jobs added")
            else:
                print("No new jobs added")

        except Exception as e:
            await self.db.rollback()
            print("Error while committing new jobs")
            print(e)

    async def get_jobs(self):
        result = await self.db.execute(select(Job))
        return result.scalars().all()

    async def get_details(self):
        possible_statuses = ['viewed', 'not_viewed', 'star']
        result = await self.db.execute(select(Job.status, func.count(Job.id)).group_by(Job.status))
        status_counts = {row[0]: row[1] for row in result}

        for status in possible_statuses:
            if status not in status_counts:
                status_counts[status] = 0

        return status_counts


async def main():
    comeet_finder = ComeetFinder('Comeet Finder', config_file.config_app.get('comeet_url'), platform_name='comeet')
    indeed_finder = IndeedFinder('Indeed Finder', config_file.config_app.get('indeed_url'), platform_name='indeed')

    async for db in get_db():
        job_service = JobService(db)
        job_service.add_finder(comeet_finder)
        job_service.add_finder(indeed_finder)
        jobs = job_service.get_jobs_from_finders()
        await job_service.update_jobs_in_db(jobs)


if __name__ == "__main__":
    asyncio.run(main())
