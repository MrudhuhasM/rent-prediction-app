"""Module for preparing the data for training the model."""

import re

import pandas as pd
from loguru import logger
from model.pipeline.collection import load_data_from_db
from sklearn.preprocessing import OrdinalEncoder


def prepare_data():
    """
    Prepare the data for training the model.

    Returns:
        _type_: Dataframe containing the data.
    """
    logger.info("Starting data preparation")
    df = load_data_from_db()
    df = encode_data(df)
    df = parse_garden_column(df)
    return df


def encode_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode the data for training the model.

    Args:
        df (pd.DataFrame): Dataframe containing the data.

    Returns:
        pd.DataFrame: Dataframe containing the encoded data.
    """
    ordinal_columns = ["balcony", "storage", "furnished", "garage", "parking"]
    logger.info(f"Encoding ordinal columns: {ordinal_columns}")
    ord_encoder = OrdinalEncoder()
    df[ordinal_columns] = ord_encoder.fit_transform(df[ordinal_columns])
    return df


def parse_garden_column(
    df: pd.DataFrame,
    parse_col: str = "garden",
) -> pd.DataFrame:
    """
    Parse the garden column.

    Args:
        df (pd.DataFrame): Dataframe containing the data.
        parse_col (str): Column to parse.   Defaults to 'garden'.

    Returns:
        pd.DataFrame: Dataframe containing the parsed data.
    """
    logger.info("Parsing garden column")
    for i, _ in enumerate(df):
        if df.loc[i, parse_col] == "Not present":
            df.loc[i, parse_col] = 0
        else:
            garden_values = re.findall(r"\d+", df.loc[i, parse_col])
            df.loc[i, parse_col] = garden_values[0] if garden_values else None
    return df
