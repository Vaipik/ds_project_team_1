from dataclasses import dataclass


class BaseImageException(Exception):
    """Base exception class for image-related exceptions."""
    
    def message(self):
        pass


@dataclass
class FileIsNotImage(BaseImageException):
    """Exception raised when a file is not a valid image.

    Attributes:
        filename (str): The filename of the invalid image.
    """
    
    filename: str

    def message(self):
        """Get the error message for the exception.

        Returns:
            str: The error message indicating that the file is not a valid image.
        """
        
        return f"{self.filename} is not valid image"


@dataclass
class CannotRecognize(BaseImageException):
    def message(self):
        return "Can't recognize object"
