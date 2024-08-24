from bs4 import BeautifulSoup
from typing import List
from config_file import config_app
from schemas.finders import Finder
from schemas.jobs import JobDetails
import requests


def get_jobs_details(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    jobs = soup.find_all('div', class_='yuRUbf')
    jobs_data = []

    for job in jobs:

        span = job.find('span')
        if not span:
            continue

        a_tag = span.find('a')
        if not a_tag:
            continue

        href = a_tag.get('href')

        if href.startswith(config_app.get('comeet_url')):
            title = href.split('/')[4]
            job_details = JobDetails(job_url=href, company_name=title,platform_name='commeet')
            jobs_data.append(job_details)

    return jobs_data


class ComeetFinder(Finder):

    def __init__(self, finder_name, finder_url,platform_name):
        super().__init__(finder_name, finder_url,platform_name)

    def get_results_by_pages(self, query, page_number):
        start = (page_number - 1) * 10
        url = f"{config_app.get('base_url')}{query.replace(' ', '+')}&start={start}"
        self.get_text()

        response = requests.get(url, headers=self.headers)
        return response.text

    def get_jobs_from_platform(self) -> List[JobDetails]:
        query = config_app.get('query')
        jobs = []

        for page in range(1, 11):
            print(f"Fetching page {page}...")
            html_content = self.get_results_by_pages(query, page)
            jobs_details = get_jobs_details(html_content)

            if not jobs_details:
                print("Stopping.")
                break

            jobs.extend(jobs_details)

        return jobs
