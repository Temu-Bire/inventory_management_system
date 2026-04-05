from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .product import Base

class SalesOrder(Base):
    __tablename__ = "sales_orders"

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String(50), unique=True, nullable=False, index=True)
    customer_name = Column(String(200))
    total_amount = Column(Float, nullable=False, default=0.0)
    notes = Column(String(500))
    status = Column(String(20), default="completed")  # completed, cancelled, etc.

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship to items
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("sales_orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)   # Price at the time of purchase
    total_price = Column(Float, nullable=False)

    # Relationships
    order = relationship("SalesOrder", back_populates="items")
    # You can add product relationship if needed for eager loading