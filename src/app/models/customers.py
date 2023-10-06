from app.models.base import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from uuid import UUID

class CustomerModel(Base):
    __tablename__ = 'customers'                                                     # tells SQLAlchemy to use the provided string as the table name in the database

    customer_id = Column(String, primary_key=True,                                  # fields required to add a new record to the database.
                        )
    customer_unique_id = Column(String, nullable=False)
    customer_zip_code_prefix  = Column(String, nullable=False)
    customer_city   = Column(String, nullable=False)
    customer_state  = Column(String, nullable=False)

    # createdAt = Column(TIMESTAMP(timezone=True),
    #                    nullable=False, server_default=func.now())
    # updatedAt = Column(TIMESTAMP(timezone=True),
    #                default=None, onupdate=func.now())