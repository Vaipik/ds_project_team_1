from fastapi import status
from fastapi.responses import JSONResponse

from src.application.exceptions.images import BaseImageException


async def file_is_not_image_handler(request, exc: BaseImageException):
    """Exception handler for FileIsNotImage exception.

    This handler is responsible for handling the FileIsNotImage exception and 
    returning an appropriate JSON response.

    Args:
        request: The request being processed.
        exc (BaseImageException): The raised FileIsNotImage exception.

    Returns:
        JSONResponse: A JSON response indicating the error message and HTTP status code.
    """
    
    return JSONResponse(
        content={
            "message": exc.message()
        },
        status_code=status.HTTP_400_BAD_REQUEST,
    )
