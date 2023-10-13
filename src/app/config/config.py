import os
from pydantic import Field, PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os

class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_HOSTNAME: str
    POSTGRES_DB: str
    POSTGRES_URL: str

    #class Config:                          #old version pydantic version 1
        #env_file = './.env'

    model_config = SettingsConfigDict(env_file="../../.env", env_file_encoding='utf-8', extra='ignore')  #new version pydantic

    # if os.environ["APP_SETTINGS"] == 'local_docker':
    #     POSTGRES_DB = 'db'
    # else:
    #     POSTGRES_DB = 'localhost'

    # POSTGRES_URL = settings.db_url #"postgresql://user:password@postgresserver/db"
    # POSTGRES_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"
    # POSTGRES_URL = "postgresql://postgres:postgres@db:5432/default_database"
    # POSTGRES_URL = "postgresql://postgres:postgres@localhost:5434/default_database"


@lru_cache                          #helps in reducing the execution time of the function by using memoization technique.
def get_settings() -> Settings:

    settings = Settings()

    return settings


