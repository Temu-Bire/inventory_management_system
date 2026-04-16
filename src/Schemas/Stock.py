from pydantic import BaseModel

class StockCreate(BaseModel):
    product_id: int
    quantity: int

class StockResponse(BaseModel):
    id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True