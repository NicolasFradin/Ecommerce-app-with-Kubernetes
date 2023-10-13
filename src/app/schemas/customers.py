from datetime import datetime
from typing import List, Optional, Union, Dict
from pydantic import BaseModel
from pydantic.types import UUID, constr
from uuid import uuid4
from datetime import datetime

class CustomerBase(BaseModel):
    customer_id: UUID = uuid4()                          #As it's not an INT primary key, it is not incremented automatically
    customer_unique_id: UUID = uuid4()                   #Genereated value by default
    customer_zip_code_prefix: Optional[str]
    customer_city: Optional[str]
    customer_state: Optional[str]                        #Optional[X] is equivalent to X | None (or Union[X, None]).
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime]

    #@validator('customer_zip_code_prefix')
    #def prevent_none(cls, v):
    #    assert v is not None, 'customer_zip_code_prefix may not be None'
    #    return v


class CustomerCreate(CustomerBase):
    customer_zip_code_prefix: Optional[constr(min_length=1, max_length=10)] = None #type method for constraining strs
    customer_city: Optional[constr(min_length=1, max_length=50)] = None
    customer_state: Optional[constr(min_length=1, max_length=5)] = None

    class Config:
        json_schema_extra = {
            "example": {
                "customer_zip_code_prefix": "75000",
                "customer_city": "Paris",
                "customer_state": "FR"
            }
        }

class CustomerUpdate(CustomerBase):
    updated_at: Optional[datetime] = datetime.now()


class Config:
        json_schema_extra = {
            "example": {
                "customer_zip_code_prefix": "92000",
                "customer_city": "Nanterre",
                "customer_state": "FR"
            }
        }

class Customer(CustomerCreate):

    class Config:                                   #the Config class tells Pydantic to map the models to ORM objects. This is required since we’re using SQLAlchemy ORM in the project
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

