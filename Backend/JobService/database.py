from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import MetaData
from collections.abc import AsyncGenerator
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_URL')}"

metadata = MetaData()

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session