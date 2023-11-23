from pydantic import BaseModel


class Sweet(BaseModel):
    name: str
    description: str | None = None
    category_id: int


class Category1(BaseModel):
    category: str
