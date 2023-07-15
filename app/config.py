from pydantic_settings import BaseSettings

class MySettings(BaseSettings):
    host: str
    port: int
    reload: bool
    postgres: str
    redis: str

    class Config:
        env_file = "../venv/.env"

settings = MySettings()
