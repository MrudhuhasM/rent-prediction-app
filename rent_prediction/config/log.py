"""Module for configuring the logger."""

from dotenv import load_dotenv
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class LoggerSettings(BaseSettings):
    """Configure the logger.

    Settings class for the application.

    Args:
        BaseSettings (_type_): _description_
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8",
    )

    log_level: str


def configure_logger(log_level: str):
    """Configure the logger.

    Logger configuration function.

    Args:
        log_level (str): The log level to set the logger to.
    """
    logger.remove()
    logger.add(
        "logs/{time}.log",
        rotation="1 week",
        retention="10 days",
        compression="zip",
        level=log_level,
    )


configure_logger(LoggerSettings().log_level)
