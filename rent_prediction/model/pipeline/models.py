"""Description: This module contains the functions to build the model."""

import pickle as pkl
from typing import Tuple

import numpy as np
import pandas as pd
from config import model_settings
from loguru import logger
from model.pipeline.preperation import prepare_data
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split


def build_model() -> None:
    """Build the model."""
    logger.info("Building the model")
    df = prepare_data()
    x, y = get_x_y(df)
    x_train, x_test, y_train, y_test = split_data(x, y)
    model = train_model(x_train, y_train)
    evaluate_model(model, x_test, y_test)
    save_model(model)


def get_x_y(df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
    """
    Get the X and y values from the dataframe.

    Args:
        df (pd.DataFrame): Dataframe containing the data.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Tuple containing the X and y values.
    """
    final_columns = [
        "area",
        "constraction_year",
        "rooms",
        "bedrooms",
        "bathrooms",
        "balcony",
        "storage",
        "parking",
        "furnished",
        "garage",
        "garden",
    ]

    x = df[final_columns].values
    y = df["rent"].values

    logger.info("Defining X and y values")

    return x, y


def split_data(
    x: np.ndarray,
    y: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Split the data into training and testing sets.

    Args:
        x (np.ndarray): Array containing the x values.
        y (np.ndarray): Array containing the y values.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        Tuple containing the X_train, X_test, y_train, and y_test values.
    """
    logger.info("Splitting data into training and testing sets")
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
    )
    return x_train, x_test, y_train, y_test


def train_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
) -> RandomForestRegressor:
    """
    Train the model.

    Args:
        X_train (np.ndarray): Array containing the X_train values.
        y_train (np.ndarray): Array containing the y_train values.

    Returns:
        RandomForestRegressor: Trained model.
    """
    logger.info("Training the model")
    rf = RandomForestRegressor()
    param_grid = {"n_estimators": [100, 200, 300], "max_depth": [10, 20, 30]}
    grid_search = GridSearchCV(rf, param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_


def evaluate_model(
    model: RandomForestRegressor,
    X_test: np.ndarray,
    y_test: np.ndarray,
) -> None:
    """
    Evaluate the model.

    Args:
        model (RandomForestRegressor): Trained model.
        X_test (np.ndarray): Array containing the X_test values.
        y_test (np.ndarray): Array containing the y_test values.
    """
    score = model.score(X_test, y_test)
    logger.info(f"Evaluating the model. Score: {score}")


def save_model(model: RandomForestRegressor) -> None:
    """
    Save the model.

    Args:
        model (RandomForestRegressor): Trained model.
    """
    logger.info("Saving the model")
    with open(
        f"{model_settings.models_path}/{model_settings.models_name}",
        "wb",
    ) as model_file:
        pkl.dump(model, model_file)
