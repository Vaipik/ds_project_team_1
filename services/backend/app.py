from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from src import init_app
from src.config import load_config


config = load_config()
app = init_app(FastAPI(
    version=config.api.version,
    ))

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.api.host,
        port=config.api.port
    )
