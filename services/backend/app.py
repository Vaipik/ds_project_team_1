from fastapi import FastAPI
import uvicorn

from src import init_app
from src.config import load_config


config = load_config()
app = init_app(FastAPI(
    version=config.api.version,
    ))


if __name__ == "__main__":
    
    uvicorn.run(
        app,
        host=config.api.host,
        port=config.api.port
    )
