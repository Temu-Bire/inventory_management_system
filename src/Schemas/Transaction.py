from pydantic import BaseModel

class StockMovementCreate(BaseModel):
    product_id: int
    type: str  # IN or OUT
    quantity: int

class StockMovementResponse(BaseModel):
    id: int
    product_id: int
    type: str  # IN or OUT
    quantity: int

    class Config:
        orm_mode = True