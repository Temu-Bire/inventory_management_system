from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str
    description: str

class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True