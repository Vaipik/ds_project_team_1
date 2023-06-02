from dataclasses import dataclass


class BaseImageException(Exception):
    def message(self):
        pass


@dataclass
class FileIsNotImage(BaseImageException):
    filename: str

    def message(self):
        return f"{self.filename} is not valid image"
