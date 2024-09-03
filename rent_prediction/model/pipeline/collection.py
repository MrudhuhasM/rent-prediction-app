"""Load data from a URL."""

import pandas as pd
from config import engine
from db.db_model import RentAppartments
from loguru import logger
from sqlalchemy import select


def load_data_from_db() -> pd.DataFrame:
    """
    Load data from the database.

    Returns:
        pd.DataFrame: Dataframe containing the data.
    """
    logger.info("Loading data from database")
    querry = select(RentAppartments)
    return pd.read_sql(querry, engine)


def load_data(url: str) -> pd.DataFrame:
    """
    Load data from a URL.

    Args:
        url (str): URL to the data.

    Returns:
        pd.DataFrame: Dataframe containing the data.
    """
    logger.info(f"Loading data from {url}")
    return pd.read_csv(url)
