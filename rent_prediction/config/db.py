"""Database configuration module."""

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine

load_dotenv()


class DbSettings(BaseSettings):
    """
    Settings class for the application.

    Args:
        BaseSettings (_type_): _description_
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8",
    )

    db_connection_string: str
    table_name: str


db_settings = DbSettings()
engine = create_engine(db_settings.db_connection_string)
