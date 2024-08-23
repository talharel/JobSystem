from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from routers.jobs import router as jobs_router
from models import jobs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
)

app.include_router(jobs_router)



jobs.Base.metadata.create_all(bind=engine)
