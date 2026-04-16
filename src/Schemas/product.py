from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    selling_price: float
    category_id: int
    supplier_id: int

class ProductUpdate(BaseModel):
    name: str
    description: str
    selling_price: float
    category_id: int
    supplier_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    selling_price: float
    category_id: int
    supplier_id: int

    class Config:
        orm_mode = True