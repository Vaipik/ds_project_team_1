from fastapi import FastAPI
import uvicorn

from src.handlers import bind_exception_handlers
from src.config import load_config
from src.routers import bind_router_handlers


def init_app(app: FastAPI) -> FastAPI:
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
