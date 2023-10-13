from app.models.base import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Integer, Double
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from uuid import UUID

class ItemModel(Base):
    __tablename__ = 'items'                                                     # tells SQLAlchemy to use the provided string as the table name in the database

    order_id = Column(String, nullable=False)
    order_item_id = Column(Integer, nullable=False, primary_key=True)
    product_id = Column(String, nullable=False)
    seller_id = Column(String, nullable=False)
    shipping_limit_date = Column(TIMESTAMP(timezone=True), nullable=True)
    price = Column(Double, nullable=False)
    freight_value = Column(Double, nullable=True)

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True),
                        default=None, onupdate=func.now())