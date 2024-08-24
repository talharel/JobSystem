from typing import List
from schemas.finders import Finder
from schemas.jobs import JobDetails
from bs4 import BeautifulSoup


def get_job_details(text, url) -> List[JobDetails]:
    soup = BeautifulSoup(text, 'html.parser')
    jobs = soup.find_all('li', class_='css-5lfssm eu4oa1w0')

    jobs_details = []

    for job in jobs:
        span = job.find('span')
        if span:
            title = span.text
            if title.find('Junior') != -1:
                job_details = JobDetails(title, url,'indeed')
                jobs_details.append(job_details)

    return jobs_details


class IndeedFinder(Finder):

    def __init__(self, finder_name, finder_url,platform_name):
        super().__init__(finder_name, finder_url,platform_name)

    def get_jobs_from_platform(self) -> List[JobDetails]:
        text = self.get_text()
        jobs_details = get_job_details(text, self.finder_url)
        return jobs_details

