from typing import Annotated

from fastapi import APIRouter, UploadFile, File, status
import tensorflow as tf

from src.application.exceptions.images import FileIsNotImage
from src.schemas.images import ImageResponse
from src.services.images import check_is_file_image, predict_object


images_router = APIRouter(
    prefix="/images",
    tags=["Images recognition"]
)

model = tf.keras.models.load_model("/app/model/efficientnetb1-cifar.h5")  # TODO: How to remove global ?


@images_router.post(
    "/",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Uploaded file is not image"
        }
    },
    response_model=ImageResponse,
)
async def predict_image(file: Annotated[UploadFile, File()]):
    file_is_image = check_is_file_image(file.content_type)
    if not file_is_image:
        raise FileIsNotImage(file.filename)
    file_content = await file.read()
    predicted_label = predict_object(model, file_content)

    return ImageResponse(label=predicted_label)
