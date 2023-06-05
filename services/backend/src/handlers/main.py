from fastapi import FastAPI

from src.application.exceptions.images import FileIsNotImage
from src.handlers.images.exception_handlers import file_is_not_image_handler


def bind_exception_handlers(app: FastAPI) -> FastAPI:
    """Bind exception handlers to the FastAPI application.

    This function registers an exception handler for the `FileIsNotImage` 
    exception, associating it with the `file_is_not_image_handler` function.

    Args:
        app (FastAPI): The FastAPI application instance.

    Returns:
        FastAPI: The FastAPI application instance with the exception handler registered.
    """
    
    app.add_exception_handler(FileIsNotImage, file_is_not_image_handler)
    return app
