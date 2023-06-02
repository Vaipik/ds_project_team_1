from fastapi import FastAPI
import tensorflow as tf
from starlette.responses import JSONResponse

from src.handlers import bind_exception_handlers
from src.routers import bind_router_handlers
from src.routers.images import images_router


# def init_app(app: FastAPI) -> FastAPI:
#     bind_exceptions(app)
#     bind_routers(app)
#     return app

app = FastAPI()
bind_exception_handlers(app)
bind_router_handlers(app)

#
# if __name__ == "__main__":
#     app = init_app(FastAPI())
