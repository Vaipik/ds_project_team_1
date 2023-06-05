from io import BytesIO
from typing import Any

from fastapi import UploadFile
import numpy as np
from PIL import Image
import tensorflow as tf

from src.schemas.images import ObjectCategories


def check_is_file_image(content_type: str) -> bool:
    """Check if the given content type indicates an image.

    Args:
        content_type (str): The content type of the file.

    Returns:
        bool: True if the content type indicates an image, False otherwise.
    """
    
    return "image" in content_type


def preprocess_image(image_content: bytes) -> Image:
    """Preprocess the image content.

    This function opens the image, resizes it to (32, 32), converts it to a NumPy array,
    and expands the dimensions to match the input shape expected by the model.

    Args:
        image_content (bytes): The content of the image.

    Returns:
        Image: The preprocessed image as a PIL Image instance.
    """
    
    image = Image.open(BytesIO(image_content))
    image = image.resize((32, 32))
    image = tf.keras.preprocessing.image.img_to_array(image)
    return np.expand_dims(image, axis=0)


def predict_object(model, image_content: bytes) -> str:
    """Predict the object category of the given image.

    This function preprocesses the image content, feeds it to the provided model for prediction,
    and returns the predicted object category as a string.

    Args:
        model (Any): The model used for prediction.
        image_content (bytes): The content of the image.

    Returns:
        str: The predicted object category.
    """
    
    processed_image = preprocess_image(image_content)
    prediction = model.predict(processed_image)
    return ObjectCategories(np.argmax(prediction[0])).name
