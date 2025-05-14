from pydantic import BaseModel


class Book(BaseModel):
    title: str
    text: str
    author: str
