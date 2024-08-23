from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.jobs import Job
from database import get_db
from celery_tasks.jobs import celery_task_update_jobs
from services.jobs import JobService

router = APIRouter(
    prefix='/jobs',
    tags=['jobs']
)


async def get_job_service() -> JobService:
    return JobService()


@router.get('/')
async def get_jobs(db: Session = Depends(get_db), jobService=Depends(JobService)):
    jobs = await jobService.get_jobs(db)
    count = len(jobs)
    return {'jobs': jobs, 'count': count}


# @router.get('/details')
# async def get_jobs(db: Session = Depends(get_db),jobService=Depends(JobService)):
#     details = await jobService.get_details(db)
#     return {'details': details}


@router.get('/abcd')
async def update_jobs():
    jobs_task = celery_task_update_jobs.delay()
    return {'status': 'sent'}
