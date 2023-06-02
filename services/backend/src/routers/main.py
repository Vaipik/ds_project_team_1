from fastapi import FastAPI

from .images import images_router


def bind_router_handlers(app: FastAPI) -> FastAPI:
    app.include_router(images_router)
    return app
