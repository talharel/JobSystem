from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.jobs import Job
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from celery_tasks.jobs import celery_task_update_jobs
from services.jobs import JobService

router = APIRouter(
    prefix='/jobs',
    tags=['jobs']
)


def get_job_service(db: AsyncSession = Depends(get_db)) -> JobService:
    return JobService(db)


@router.get('/')
async def get_jobs(job_service: JobService = Depends(get_job_service)):
    jobs = await job_service.get_jobs()
    jobs_count = len(jobs)
    return {'jobs': jobs, 'count': jobs_count}



@router.get('/details')
async def get_details(job_service: JobService = Depends(get_job_service)):
    jobs_details = await job_service.get_details()
    return {'details':jobs_details}



@router.get('/abcd')
async def update_jobs():
    jobs_task = celery_task_update_jobs.delay()
    return {'status': 'Task Sent'}
