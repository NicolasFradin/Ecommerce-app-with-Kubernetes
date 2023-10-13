from datetime import datetime
from typing import List, Optional, Union, Dict
from pydantic import BaseModel
from pydantic.types import UUID, constr
from uuid import uuid4
from datetime import datetime


class OrderBase(BaseModel):
    order_id: UUID = uuid4()                          #As it's not an INT primary key, it is not incremented automatically
    customer_id: UUID = uuid4()                       #Genereated value by default
    order_status: str = 'pending'
    order_purchase_timestamp: datetime = datetime.now()
    order_approved_at: datetime = datetime.now()
    order_delivered_carrier_date: Optional[datetime] = datetime.now()
    order_delivered_customer_date: Optional[datetime] = datetime.now()
    order_estimated_delivery_date: Optional[datetime] = datetime.now()

    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    #@validator('order_zip_code_prefix')
    #def prevent_none(cls, v):
    #    assert v is not None, 'order_zip_code_prefix may not be None'
    #    return v


class OrderCreate(OrderBase):
    pass

    class Config:
        json_schema_extra = {
            "example": {
                "order_id": uuid4(),
                "customer_id": uuid4(),
                "order_status": 'pending',
                "order_purchase_timestamp": datetime.now(),
                "order_approved_at": datetime.now(),
                "order_delivered_carrier_date": datetime.now(),
                "order_delivered_customer_date": datetime.now(),
                "order_estimated_delivery_date": datetime.now(),
            }
        }

class OrderUpdate(OrderBase):
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        json_schema_extra = {
            "example": {
                "order_status": 'sent',
            }
        }

class Order(OrderCreate):

    class Config:                                   #the Config class tells Pydantic to map the models to ORM objects. This is required since we’re using SQLAlchemy ORM in the project
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

