import os

from sqlalchemy.orm import Session
from sqlmodel import create_engine, SQLModel, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv

pool_size = int(os.getenv("DATABASE_POOL_SIZE", "10"))
# engine = create_engine("postgresql+psycopg2://postgres:example@host.docker.internal:5433/postgres")
# engine = create_engine("postgresql+psycopg2://postgres:example@localhost:5433/postgres")
# engine = create_engine(os.getenv("DATABASE_ENGINE"))

database_url = os.getenv(
    "DATABASE_URL"
)

engine = create_engine(
    url=database_url,
    pool_size=10,
    max_overflow=20,
    pool_recycle=3600,
    pool_pre_ping=True
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def check_availability() -> bool:
    try:
        with Session(engine) as session:
            session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print(e)
        return False
