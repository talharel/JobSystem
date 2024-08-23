from fastapi import Depends
from sqlalchemy.orm import Session
from models.jobs import Job
from database import get_db
from finders.comeet_finder import ComeetFinder
from finders.indeed_finder import IndeedFinder
from typing import List
from schemas.jobs import JobDetails
from schemas.finders import Finder
import config_file


class JobService:

    def __init__(self):
        self.finders = []

    def add_finder(self, finder: Finder):
        if not isinstance(finder, Finder):
            raise Exception('Not a Finder Instance')

        self.finders.append(finder)

    def get_jobs_from_finders(self) -> List[JobDetails]:
        jobs = []
        for finder in self.finders:
            try:
                found_jobs = finder.get_jobs()
                jobs.extend(found_jobs)
            except Exception as e:
                print(f"Failed to fetch jobs from {finder.finder_name}: {str(e)}")
        return jobs

    def update_jobs_in_db(self, jobs):
        db = next(get_db())
        try:

            existing_urls = {job.url for job in db.query(Job).all()}
            new_jobs = [Job(company_name=job.company_name, url=job.job_url, status='not_viewed',
                            platform_name=job.platform_name) for job in jobs if
                        job.job_url not in existing_urls]

            if new_jobs:
                db.add_all(new_jobs)
                db.commit()
            else:
                print("No new jobs to add.")

        except Exception as e:
            db.rollback()
            print("Error while committing new jobs")
            print(e)
        finally:
            db.close()

    async def get_jobs(self, db: Session = Depends(get_db)):
        try:
            jobs = await db.query(Job).all()
            return jobs
        except Exception as e:
            print(e)

    def get_details(self):
        pass


if __name__ == "__main__":
    comeet_finder = ComeetFinder('Comeet Finder', config_file.config_app.get('comeet_url'), platform_name='comeet')
    indeed_finder = IndeedFinder('Indeed Finder', config_file.config_app.get('indeed_url'), platform_name='indeed')

    jobService = JobService()
    jobService.add_finder(comeet_finder)
    jobService.add_finder(indeed_finder)
    jobs = jobService.get_jobs_from_finders()
    jobService.update_jobs_in_db(jobs)
