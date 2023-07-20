from pydantic_settings import BaseSettings


class MySettings(BaseSettings):
    HOST: str
    PORT: str
    RELOAD: bool
    POSTGRES: str
    REDIS: str
    POSTGRES_MIG: str
    
    class Config:
        env_file = ".env"

settings = MySettings()