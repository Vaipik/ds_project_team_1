from fastapi import FastAPI

from .images import images_router


def bind_router_handlers(app: FastAPI) -> FastAPI:
    """Bind router handlers to the FastAPI application.

    This function includes the `images_router` in the FastAPI application, making the image-related routes available.

    Args:
        app (FastAPI): The FastAPI application instance.

    Returns:
        FastAPI: The FastAPI application instance with the router handlers bound.
    """
    
    app.include_router(images_router)
    return app
