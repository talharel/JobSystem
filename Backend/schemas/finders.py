from abc import ABC, abstractmethod
from schemas.jobs import JobDetails
from config_file import config_app
from typing import List
import requests


class Finder(ABC):
    headers = {
        "User-Agent": config_app.get('header')
    }

    def __init__(self, finder_name, finder_url,platform_name):
        self.finder_name = finder_name
        self.finder_url = finder_url
        self.platform_name = platform_name

    def get_text(self):
        try:
            response = requests.get(self.finder_url, headers=self.headers)
            return response.text
        except Exception as e:
            print(f'Cant get data from {self.finder_name}')
            print(f'Exception {e}')

    @abstractmethod
    def get_jobs(self) -> List[JobDetails]:
        pass
