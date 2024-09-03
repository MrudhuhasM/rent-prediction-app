"""
Module for the ML model settings.

This module contains the settings for the ML model
used in the application.
"""

from dotenv import load_dotenv
from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class ModelSettings(BaseSettings):
    """
    ML model Settings class for the application.

    Args:
        BaseSettings (_type_): _description_
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8",
    )

    models_path: DirectoryPath
    models_name: str


model_settings = ModelSettings()
