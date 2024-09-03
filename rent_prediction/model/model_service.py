"""
This module contains the ModelService class.

This class is responsible for loading the model and predicting the rent.
"""

import pickle as pkl
from pathlib import Path

from config import model_settings
from loguru import logger
from model.pipeline.models import build_model


class ModelService:
    """
    Class to load and predict using the model.

    This class is responsible for loading the model and predicting the rent.

    Attributes:
        model (object): Model object.

    Methods:
        load_model: Load the model.
        predict: Predict the rent.
    """

    def __init__(self):
        """Initialize the model attribute."""
        self.model = None

    def load_model(
        self,
        models_name: str = model_settings.models_name,
    ) -> None:
        """Load the model.

        Args:
            models_name (str): Model name.
                Defaults to settings.models_name.
        """
        logger.info(
            f"Loading model: {models_name} from {model_settings.models_path}",
        )
        models_path = Path(f"{model_settings.models_path}/{models_name}")

        if not models_path.exists():
            logger.warning(
                f"Model {model_settings.models_name} not found",
                f"at {model_settings.models_path}",
                f"Building model -> {model_settings.models_name}",
            )
            build_model()

        logger.info(f"Succesfully loaded model {models_name}")
        with open(models_path, "rb") as model_file:
            self.model = pkl.load(model_file)

    def predict(self, X: list) -> list:
        """
        Predict the rent.

        Args:
            X (list): List containing the features.

        Returns:
            list: Predicted rent.
        """
        logger.info(f"Predicting rent for features: {X}")
        return self.model.predict([X])
