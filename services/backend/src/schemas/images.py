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


class ImageResponse(BaseModel):
    label: str = Field(alias="imageClass")

    class Config:
        allow_population_by_field_name = True
