"""
This module is the entry point of the application.

This module is the entry point of the application.
It loads the model and predicts the rent for a given set of features.
"""

from loguru import logger
from model.model_service import ModelService


@logger.catch
def main() -> None:
    """Run the main function of the application."""
    logger.info("Starting the application")
    model_service = ModelService()
    model_service.load_model()
    feature_values = {
        "area": 100,
        "constraction_year": 1990,
        "rooms": 3,
        "bedrooms": 2,
        "bathrooms": 2,
        "balcony": 1,
        "storage": 1,
        "parking": 1,
        "furnished": 1,
        "garage": 1,
        "garden": 1,
    }
    prediction = model_service.predict(list(feature_values.values()))
    logger.info(f"Predicted rent: {prediction}")


if __name__ == "__main__":
    main()
