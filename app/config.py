from pydantic_settings import BaseSettings

class MySettings(BaseSettings):
    host: str
    port: int
    reload: bool

    class Config:
        env_file = "../venv/.env"