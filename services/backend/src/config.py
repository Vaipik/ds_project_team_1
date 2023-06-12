from pydantic import BaseSettings
import tensorflow as tf


model_c10 = tf.keras.models.load_model("/app/model/efficientnetb1-cifar.h5")
model_c100 = tf.keras.models.load_model("/app/model/efficientnetV2B1-cifar100.h5")


class APISettings(BaseSettings):
    version: str
    host: str
    port: int


class Settings(BaseSettings):
    api: APISettings

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


def load_config(env_file=".env") -> Settings:
    return Settings(env_file)
