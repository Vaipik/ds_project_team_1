from fastapi import FastAPI

from src.application.exceptions.images import FileIsNotImage
from src.handlers.images.exception_handlers import file_is_not_image_handler


def bind_exception_handlers(app: FastAPI) -> FastAPI:
    app.add_exception_handler(FileIsNotImage, file_is_not_image_handler)
    return app
