from typing import Annotated

from fastapi import APIRouter, UploadFile, File, status

from src.application.exceptions.images import FileIsNotImage, CannotRecognize
from src.config import model_c10, model_c100
from src.application.constants import images as constants
from src.schemas.images import ImageResponse
from src.services.images import check_is_file_image, predict_object
from src.utils.cifar_labels import CIFAR_LABELS


images_router = APIRouter(
    prefix="/images",
    tags=["Images recognition"]
)


@images_router.post(
    "/cifar/{cifar}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Uploaded file is not image"
        }
    },
    response_model=ImageResponse,
)
async def predict_image(cifar: int, file: Annotated[UploadFile, File()]):
    """Predict the label of an uploaded image.

    This endpoint accepts a file upload and predicts the label of the image using a pre-trained model.

    Args:
        cifar (int): version of cifar dataset
        file (UploadFile): The uploaded image file.


    Returns:
        ImageResponse: The response containing the predicted label of the image.

    Raises:
        FileIsNotImage: If the uploaded file is not a valid image file.

    """
    
    file_is_image = check_is_file_image(file.content_type)
    if not file_is_image:
        raise FileIsNotImage(file.filename)
    file_content = await file.read()
    labels = CIFAR_LABELS.get(f"CIFAR-{cifar}")
    model = model_c10 if cifar == 10 else model_c100
    predicted_label, probability = predict_object(model, file_content, labels)
    if probability < constants.MIN_PROBABILITY:
        raise CannotRecognize 
    return ImageResponse(label=predicted_label, probability=probability)
