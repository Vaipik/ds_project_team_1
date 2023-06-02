from io import BytesIO
from typing import Any

from fastapi import UploadFile
import numpy as np
from PIL import Image
import tensorflow as tf


def check_is_file_image(content_type: str) -> bool:
    return "image" in content_type


def preprocess_image(image_content: bytes) -> Image:
    image = Image.open(BytesIO(image_content))
    image = image.resize((32, 32))
    image = tf.keras.preprocessing.image.img_to_array(image)

    return np.expand_dims(image, axis=0)


def predict_object(model, image_content: bytes) -> str:
    classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']  # TODO: remove from function
    processed_image = preprocess_image(image_content)
    prediction = model.predict(processed_image)
    prediction_label = classes[np.argmax(prediction[0])]
    return prediction_label
