from decimal import Decimal

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    price: Decimal = Field(..., gt=0)
    reorder_point: int = Field(0, ge=0)          # When to trigger low-stock alert
    category: Optional[str] = Field(None, max_length=100)

class ProductCreate(ProductBase):
    initial_stock: int = Field(0, ge=0)

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    price: Optional[Decimal] = Field(None, gt=0)
    reorder_point: Optional[int] = Field(None, ge=0)
    category: Optional[str] = None

class ProductResponse(ProductBase):
    id: int
    current_stock: int
    is_low_stock: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)  # Allows reading from SQLAlchemy objects