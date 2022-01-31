import datetime
import os.path
import secrets

from pydantic import BaseSettings
import app


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str = secrets.token_urlsafe(32)

    ACCESS_TOKEN_EXPIRE_MINUTES: int = datetime.timedelta(days=8)

    BASE_DIR = os.path.dirname(os.path.abspath(app.__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'database.db')


settings = Settings()
