from pydantic import BaseModel


class Sweet(BaseModel):
    name: str
    description: str | None = None
    category_id: int
    img: str | None = None


class Category1(BaseModel):
    category: str


class Response1(BaseModel):
    comment: str


