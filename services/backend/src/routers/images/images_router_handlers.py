from typing import Annotated

from fastapi import APIRouter, UploadFile, File, status

from src.application.exceptions.images import FileIsNotImage
from src.schemas.images import FileIsNotImageSchema, ImageResponse
from src.services.images import check_is_file_image


images_router = APIRouter(
    prefix="/images",
    tags=["Images recognition"]
)

model = tf.keras.models.load_model("")  # TODO: How to remove global ?


@images_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": {
                "message": "Uploaded file is not image"
            }
        }
    },
    response_model=ImageResponse
)
def predict_image(file: Annotated[UploadFile, File()]):
    file_is_image = check_is_file_image(file.content_type)
    if not file_is_image:
        raise FileIsNotImage(file.filename)

    predict_object
    return file
