from celery_worker import celery_app
from services.companies import CompanyService
from database import get_db
from bs4 import BeautifulSoup
from config_file import config_app
import requests


def check_term_in_page(url, word='Junior'):
    try:
        response = requests.get(url, headers={
            "User-Agent": config_app.get('header')
        })
        soup = BeautifulSoup(response.text, 'html.parser')
        if word.lower() in soup.get_text().lower():
            return True
        return False
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return False


async def search_word_in_companies(word: str):
    async for db in get_db():
        companyService = CompanyService(db)
        all_companies = await companyService.get_companies()
        companies = [company.company_name for company in all_companies if check_term_in_page(url=company.url, word=word)]
        return companies


@celery_app.task(bind=True, acks_late=True)
def celery_task_find_word_in_companies(self, companies, word: str):
    try:
        company_list_contains_word = [company['id'] for company in companies if check_term_in_page(url=company['url'], word=word)]
        return company_list_contains_word
    except Exception as e:
        print(e)
        self.retry(countdown=4)
