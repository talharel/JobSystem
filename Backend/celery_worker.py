from celery import Celery
from dotenv import load_dotenv
import os


load_dotenv()
backend = f"db+postgresql://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_URL')}"

celery_app = Celery('celery_tasks',
                    broker='amqp://guest:guest@localhost:5672/',
                    backend=backend,
                    include=['celery_tasks.jobs','celery_tasks.companies'])
