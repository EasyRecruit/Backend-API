from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    APP_KEY: str

    class Config:
        env_file = "settings/.env"


@lru_cache()
def Env():
    return Settings()
