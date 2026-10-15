import os
from pydantic_settings import BaseSettings,SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):
    database_url:str=os.getenv("DATABASE_URL");
    model_config=SettingsConfigDict(env_file=".env",env_file_encoding="utf-8",extra="ignore")
Settings=Settings()
