from fastapi import status
from fastapi.responses import JSONResponse

from src.application.exceptions import images


async def file_is_not_image_handler(request, exc: images.BaseImageException):
    """Exception handler for FileIsNotImage exception.

    This handler is responsible for handling the FileIsNotImage exception and 
    returning an appropriate JSON response.

    Args:
        request: The request being processed.
        exc (BaseImageException): The raised FileIsNotImage exception.

    Returns:
        JSONResponse: A JSON response indicating the error message and HTTP status code.
    """
    match exc:
        case images.FileIsNotImage():
            return JSONResponse(
                content={
                    "message": exc.message()
                },
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            )
        case images.CannotRecognize():
            return JSONResponse(
                content={
                    "message": exc.message()
                },
                status_code=status.HTTP_400_BAD_REQUEST,
            )
