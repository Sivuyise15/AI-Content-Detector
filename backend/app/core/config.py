from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    ALLOWED_ORIGINS: str = "http://localhost:3000"
    MODEL_NAME: str = "roberta-base-openai-detector"
    MODEL_CACHE_DIR: str = "./ml_models/cache"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"

settings = Settings()