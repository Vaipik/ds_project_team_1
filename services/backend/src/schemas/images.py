from enum import Enum

from pydantic import BaseModel, Field


class ObjectCategories(str, Enum):
    airplane = "airplane"
    automobile = "automobile"
    bird = "bird"
    cat = "cat"
    deer = "deer"
    dog = "dog"
    frog = "frog"
    horse = "horse"
    ship = "ship"
    truck = "truck"


class FileIsNotImageSchema(BaseModel):
    message: str


class ImageResponse(BaseModel):
    class_: ObjectCategories = Field(alias="imageClass")
