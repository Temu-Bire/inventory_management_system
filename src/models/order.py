from pydantic import BaseModel, Field, computed_field
from typing import List, Optional
from datetime import datetime
from enum import Enum


# ORDER STATUS
class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


class OrderItem(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)
    price: float = Field(..., gt=0)

    @computed_field
    @property
    def total(self) -> float:
        return self.quantity * self.price


class Order(BaseModel):
    order_id: Optional[int] = None
    customer_name: str

    items: List[OrderItem]

    # DISCOUNT (%)
    discount_percent: float = Field(default=0, ge=0, le=100)

    # VAT (%)
    vat_percent: float = Field(default=15, ge=0)
    status: OrderStatus = OrderStatus.PENDING

    created_at: datetime = datetime.now()

    # subtotal
    @computed_field
    @property
    def subtotal(self) -> float:
        return sum(item.total for item in self.items)

    # discount amount
    @computed_field
    @property
    def discount_amount(self) -> float:
        return (self.subtotal * self.discount_percent) / 100

    # VAT amount
    @computed_field
    @property
    def vat_amount(self) -> float:
        return (self.subtotal - self.discount_amount) * (self.vat_percent / 100)

    # final total
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.subtotal - self.discount_amount + self.vat_amount

    # total items
    @computed_field
    @property
    def total_items(self) -> int:
        return sum(item.quantity for item in self.items)

    # empty check
    def is_empty(self) -> bool:
        return len(self.items) == 0