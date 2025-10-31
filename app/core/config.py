from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class DBSettings(BaseModel):
    url: str = getenv(
        "DB_URL", "postgresql://postgres:password@localhost:5434/boardshop_db"
    )
    echo: bool = getenv("DB_ECHO", False)
    max_overflow: int = getenv("DB_MAX_OVERFLOW", 10)


class SRVSettings(BaseModel):
    host: str = getenv("HOST", "0.0.0.0")
    port: int = getenv("PORT", 8000)


class APIV1(BaseModel):
    prefix: str = "/v1"


class APISettings(BaseModel):
    prefix: str = "/api"
    v1: APIV1 = APIV1()


class AccessToken(BaseModel):
    lifetime_seconds: int = getenv("ACCESS_TOKEN_LIFETIME_SECONDS", 3600)


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    srv: SRVSettings = SRVSettings()
    api: APISettings = APISettings()
    access_token: AccessToken = AccessToken()


settings = Settings()
