from pydantic import BaseModel, Field


class ImageResponse(BaseModel):
    """Response model for image prediction.

    This model represents the predicted label of an image.

    Attributes:
        label (str): The predicted label of the image.
    """
    
    label: str = Field(alias="imageClass")
    probability: str = Field(alias="probability")

    class Config:
        """Pydantic configuration for the ImageResponse model.

        This configuration allows population of the model by field name.
        """
        
        allow_population_by_field_name = True
