from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from app.config.config import settings
from fastapi_utils.guid_type import setup_guids_postgresql

#POSTGRES_URL = settings.db_url #"postgresql://user:password@postgresserver/db"
#POSTGRES_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"
POSTGRES_URL = "postgresql://postgres:postgres@db:5432/default_database"
#POSTGRES_URL = "postgresql://postgres:postgres@localhost:5434/default_database"

engine = create_engine(
    POSTGRES_URL, echo=True
)
setup_guids_postgresql(engine)  #Install the pgcrypto extension of not installed on the Postgres instance.Used for generate the UUIDs.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():

    """
    function that will create a new database session and close the session after the operation has ended.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()