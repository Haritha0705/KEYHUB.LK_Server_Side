import os
from typing import Annotated, AsyncGenerator
from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

_APP_ENV = os.getenv("APP_ENV", "dev")
if not load_dotenv(f".env.{_APP_ENV}", override=True):
    load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True,
)
SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    session = SessionLocal()
    try:
        yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()

SessionDep = Annotated[AsyncSession, Depends(get_db)]
