from datetime import datetime
from typing import List, Optional, Union, Dict
from pydantic import BaseModel
from pydantic.types import UUID, constr, condecimal
from uuid import uuid4
from datetime import datetime
from app.schemas.orders import Order
class ItemBase(BaseModel):
    order_id: UUID = uuid4()
    order_item_id: int
    product_id: UUID = uuid4()
    seller_id: UUID = uuid4()
    shipping_limit_date: Optional[datetime]
    price: Optional[condecimal(decimal_places=2)]
    freight_value: Optional[condecimal(decimal_places=2)]
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    #@validator('item_zip_code_prefix')
    #def prevent_none(cls, v):
    #    assert v is not None, 'item_zip_code_prefix may not be None'
    #    return v

class ItemCreate(ItemBase):
    shipping_limit_date: Optional[datetime] = None
    price: Optional[condecimal(decimal_places=2)] = None
    freight_value: Optional[condecimal(decimal_places=2)] = None

    class Config:
        json_schema_extra = {
            "example": {
                "order_id": uuid4(),
                "product_id": uuid4(),
                "seller_id": uuid4(),
                "order_item_id": 1,
                "shipping_limit_date": datetime.now(),
                "price": 50.00,
                "freight_value": 100.00
            }
        }

class ItemUpdate(ItemBase):
    pass

    class Config:
        json_schema_extra = {
            "example": {
                "order_id": uuid4(),
                "product_id": uuid4(),
                "seller_id": uuid4(),
                "order_item_id": 1,
                "shipping_limit_date": datetime.now(),
                "price": 10.00,
                "freight_value": 3.00
            }
        }

class Item(ItemCreate):

    class Config:                                   #the Config class tells Pydantic to map the models to ORM objects. This is required since we’re using SQLAlchemy ORM in the project
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True