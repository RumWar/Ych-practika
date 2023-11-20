from pydantic import BaseModel


class Sweet(BaseModel):
    name: str
    description: str | None = None