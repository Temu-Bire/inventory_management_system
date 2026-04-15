from os import times

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.database import Base

class StockMovement(Base):
    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))

    type = Column(String)  # IN or OUT
    quantity = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product")