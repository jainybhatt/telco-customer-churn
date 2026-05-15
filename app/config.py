from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str = "default-dev-key"
    log_level: str = "info"
    app_version: str = "1.0.0"
    
    class Config:
        env_file = ".env"

settings = Settings()