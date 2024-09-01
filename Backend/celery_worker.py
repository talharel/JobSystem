from celery import Celery

celery_app = Celery('celery_tasks',
                    broker='amqp://guest:guest@localhost:5672/',
                    backend='db+postgresql://postgres:postgresql@localhost:5433/JobQuestProDB',
                    include=['celery_tasks.jobs','celery_tasks.companies'])
