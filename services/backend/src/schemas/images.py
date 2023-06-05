from enum import Enum

from pydantic import BaseModel, Field


class ObjectCategories(Enum):
    """Enumeration of object categories.

    Each category represents a specific object class and has a corresponding numeric value.
    """
    
    airplane = 0
    automobile = 1
    bird = 2
    cat = 3
    deer = 4
    dog = 5
    frog = 6
    horse = 7
    ship = 8
    truck = 9


class ImageResponse(BaseModel):
    """Response model for image prediction.

    This model represents the predicted label of an image.

    Attributes:
        label (str): The predicted label of the image.
    """
    
    label: str = Field(alias="imageClass")

    class Config:
        """Pydantic configuration for the ImageResponse model.

        This configuration allows population of the model by field name.
        """
        
        allow_population_by_field_name = True
