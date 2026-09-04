import os
# pyrefly: ignore [missing-import]
from pydantic_settings import BaseSettings
# pyrefly: ignore [missing-import]
from pydantic import Field



class Settings(BaseSettings):
    # API configuration
    groq_api_key: str = Field(default="", validation_alias="GROQ_API_KEY")
    groq_model: str = Field(default="openai/gpt-oss-120b", validation_alias="GROQ_MODEL")
    
    # MongoDB configuration
    mongodb_url: str = Field(default="mongodb://localhost:27017", validation_alias="MONGODB_URL")
    database_name: str = Field(default="startup_consultant", validation_alias="DATABASE_NAME")
    
    # App configuration
    port: int = Field(default=8000, validation_alias="PORT")
    host: str = Field(default="127.0.0.1", validation_alias="HOST")

    class Config:
        env_file = ".env"
        extra = "ignore"




settings = Settings()
