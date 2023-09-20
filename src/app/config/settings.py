import os
from pydantic import Field
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')
    #DATABASE_PORT: int
    #POSTGRES_PASSWORD: str
    #POSTGRES_USER: str
    #POSTGRES_DB: str
    #POSTGRES_HOST: str
    #POSTGRES_HOSTNAME: str

    #class Config:
        #env_file = './.env'

settings = Settings()           #Instanciated object to import


