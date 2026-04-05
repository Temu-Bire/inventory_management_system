from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from typing import cast
from .database import Base 

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    current_stock = Column(Integer, default=0)
    reorder_point = Column(Integer, default=0)
    category = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @property
    def is_low_stock(self) -> bool:
        return cast(int, self.current_stock) <= cast(int, self.reorder_point)