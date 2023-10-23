from app.models.base import Base
from app.models.customers import CustomerModel
from app.models.items import ItemModel
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, RelationshipProperty
from uuid import UUID

class OrderModel(Base):
    __tablename__ = 'orders'                                    # tells SQLAlchemy to use the provided string as the table name in the database

    order_id = Column(String, primary_key=True)                 # fields required to add a new record to the database.
    customer_id = Column(String, ForeignKey("customers.customer_id"), nullable=False)                # You should not use Strings as columns for a uuid, for performance issues. A Binary(16) is more recommended. String uuid takes up twice the space - 16bytes vs 32 chars
    order_status  = Column(String, nullable=True)
    order_purchase_timestamp   = Column(TIMESTAMP(timezone=False), nullable=True)
    order_approved_at  = Column(TIMESTAMP(timezone=False), nullable=True)
    order_delivered_carrier_date  = Column(TIMESTAMP(timezone=False), nullable=True)
    order_delivered_customer_date  = Column(TIMESTAMP(timezone=False), nullable=True)
    order_estimated_delivery_date  = Column(TIMESTAMP(timezone=False), nullable=True)

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True,
                        default=None, onupdate=func.now())

    #Relationship
    customers = relationship("CustomerModel", back_populates="orders")
    items = relationship("ItemModel", back_populates="orders")

