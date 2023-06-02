from typing import Any

import tensorflow as tf


def check_is_file_image(content_type: str) -> bool:
    return "image" in content_type


def predict_object(obj: Any) -> str:
    return ""