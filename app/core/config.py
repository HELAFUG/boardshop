from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class DBSettings(BaseModel):
    url: str = getenv(
        "DB_URL", "postgresql://postgres:password@localhost:5434/boardshop_db"
    )
    echo: bool = False
    max_overflow: int = 10
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class SRVSettings(BaseModel):
    host: str = getenv("SERVER_HOST", "0.0.0.0")
    port: int = getenv("SERVER_PORT", 8000)


class APIV1(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"


class APISettings(BaseModel):
    prefix: str = "/api"
    v1: APIV1 = APIV1()

    @property
    def bearer_token_url(self) -> str:
        # api/v1/auth/login
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login")
        path = "".join(parts)
        # return path[1:]
        return path.removeprefix("/")


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str = getenv("RESET_PASSWORD_SECRET_TOKEN", "secret")
    verification_token_secret: str = getenv("VERIFICATION_SECRET_TOKEN", "secret")


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    srv: SRVSettings = SRVSettings()
    api: APISettings = APISettings()
    access_token: AccessToken = AccessToken()


settings = Settings()
