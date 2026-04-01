from pydantic import BaseModel, Field, computed_field
from typing import Optional
from datetime import datetime, date


class Product(BaseModel):
    product_id: Optional[int] = None
    name: str
    category: Optional[str] = None

    price: float = Field(..., gt=0)
    cost_price: float = Field(..., gt=0)

    stock_quantity: int = Field(..., ge=0)

    currency: str = "USD"  # currency support

    expiry_date: Optional[date] = None  # expiry tracking

    created_at: datetime = datetime.now()

    # LOW STOCK CHECK
    def is_low_stock(self) -> bool:
        return self.stock_quantity < 5

    # EXPIRY CHECK
    def is_expired(self) -> bool:
        if self.expiry_date:
            return date.today() > self.expiry_date
        return False

    # PROFIT PER UNIT
    @computed_field
    @property
    def profit_per_unit(self) -> float:
        return self.price - self.cost_price