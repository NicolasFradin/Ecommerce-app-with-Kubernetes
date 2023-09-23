import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOSTNAME: str

    #class Config:                          #old version pydantic version 1
        #env_file = './.env'

    model_config = SettingsConfigDict(env_file=".env")


#class DockerConfig(Base):
#    db_url: str = Field(..., env='APP_SETTINGS')



settings = Settings()           #Instanciated object to import


