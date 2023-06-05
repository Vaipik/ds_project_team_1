from pydantic import BaseSettings, RedisDsn
import tensorflow as tf


model = tf.keras.models.load_model("/app/model/efficientnetb1-cifar.h5")

class APISettings(BaseSettings):
    version: str
    host: str
    port: int


class Settings(BaseSettings):
    api: APISettings
    #redis: RedisDsn

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


def load_config(env_file=".env") -> Settings:
    settings = Settings(env_file)
    return settings
