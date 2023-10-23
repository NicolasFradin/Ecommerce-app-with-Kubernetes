from app.models.base import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from uuid import UUID

class CustomerModel(Base):
    __tablename__ = 'customers'                                            # tells SQLAlchemy to use the provided string as the table name in the database

    customer_id = Column(String, primary_key=True)             # fields required to add a new record to the database.
    customer_unique_id = Column(String, nullable=False)        # You should not use Strings as columns for a uuid, for performance issues. A Binary(16) is more recommended. String uuid takes up twice the space - 16bytes vs 32 chars
    customer_zip_code_prefix  = Column(String, nullable=True)
    customer_city   = Column(String, nullable=True)
    customer_state  = Column(String, nullable=True)

    created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True),
                        default=None, onupdate=func.now())

    #Relationship
    orders = relationship("OrderModel", back_populates="customers")