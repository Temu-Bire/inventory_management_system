from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import List, Optional

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    id: int
    unit_price: Decimal          # Price at the time of sale
    total_price: Decimal

    model_config = ConfigDict(from_attributes=True)

class SalesOrderBase(BaseModel):
    customer_name: Optional[str] = Field(None, max_length=200)
    notes: Optional[str] = None

class SalesOrderCreate(SalesOrderBase):
    items: List[OrderItemCreate] = Field(..., min_length=1)

class OrderStatus(str, Enum):
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    PENDING = "pending"
class SalesOrderResponse(SalesOrderBase):
    id: int
    order_number: str
    total_amount: Decimal
    status: OrderStatus = OrderStatus.COMPLETED
    created_at: datetime
    items: List[OrderItemResponse]

    model_config = ConfigDict(from_attributes=True)

# For reports
class LowStockAlert(BaseModel):
    product_id: int
    name: str
    current_stock: int
    reorder_point: int
    deficit: int = Field(..., ge=0)