import datetime
import os.path
import secrets

from pydantic import BaseSettings
import app


class Settings(BaseSettings):
    PROJECT_NAME: str = "Auth Service"

    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str = secrets.token_urlsafe(32)

    ACCESS_TOKEN_EXPIRE_MINUTES: int = datetime.timedelta(days=8).total_seconds()

    BASE_DIR = os.path.dirname(os.path.abspath(app.__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, os.pardir, 'database.db').replace('\\', '\\\\')

    FIRST_SUPERUSER: str = "admin@admin.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin"


settings = Settings()
