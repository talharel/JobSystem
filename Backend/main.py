from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from routers.jobs import router as jobs_router
from models.base_model import Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
)

app.include_router(jobs_router)




async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup():
    await init_models()

@app.on_event("shutdown")
async def shutdown():
    pass
