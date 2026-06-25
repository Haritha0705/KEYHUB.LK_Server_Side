import os
from typing import Annotated, Generator

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

Base = declarative_base()

# Single engine + session factory for the whole process.
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # transparently recover from dropped connections
    future=True,
)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    future=True,
)

def get_db() -> Generator[Session, None, None]:

    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


# Inject with: def endpoint(session: SessionDep): ...
SessionDep = Annotated[Session, Depends(get_db)]
