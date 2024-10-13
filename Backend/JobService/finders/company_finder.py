import requests
from bs4 import BeautifulSoup
from config_file import config_app


def check_term_in_page(url, term="Junior"):
    try:
        # Fetch the page content
        response = requests.get(url, headers={
            "User-Agent": config_app.get('header')
        })
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if the term exists in the page
        if term.lower() in soup.get_text().lower():
            return True
        return False
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return False


if __name__ == '__main__':
    urls = [
        'https://imagen-ai.com/careers/',
        'https://cadence.wd1.myworkdayjobs.com/External_Careers?Location_Country=084562884af243748dad7c84c304d89a'
    ]
    for url in urls:
        if check_term_in_page(url, 'Lead'):
            print(url)
        else:
            print(False)
