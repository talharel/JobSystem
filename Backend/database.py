from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import MetaData
from collections.abc import AsyncGenerator
from typing import Any

DATABASE_URL = "postgresql+asyncpg://postgres:postgresql@127.0.0.1:5433/JobQuestProDB"

metadata = MetaData()

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session