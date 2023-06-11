from fastapi import FastAPI

import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from src.handlers import bind_exception_handlers
from src.config import load_config
from src.routers import bind_router_handlers


def init_app(app: FastAPI) -> FastAPI:
    """Initialize the FastAPI application.

    This function binds exception handlers and router handlers to the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.

    Returns:
        FastAPI: The initialized FastAPI application instance.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8080"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    bind_exception_handlers(app)
    bind_router_handlers(app)
    return app


if __name__ == "__main__":
    config = load_config()
    app = init_app(FastAPI(
        version=config.api.version,
    ))
    uvicorn.run(
        app,
        host=config.api.host,
        port=config.api.port
    )
