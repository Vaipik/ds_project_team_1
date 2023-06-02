from fastapi import status
from fastapi.responses import JSONResponse

from src.application.exceptions.images import BaseImageException


async def file_is_not_image_handler(request, exc: BaseImageException):
    return JSONResponse(
        content={
            "message": exc.message()
        },
        status_code=status.HTTP_400_BAD_REQUEST,
    )
