from datetime import datetime
from typing import List, Optional, Union, Dict
from pydantic import BaseModel
from pydantic.types import UUID, constr
from uuid import uuid4

class CustomerBase(BaseModel):
    customer_id: UUID                           #As it's not an INT primary key, it is not incremented automatically
    customer_unique_id: UUID = uuid4()          #Genereated value by default
    customer_zip_code_prefix: Optional[str]
    customer_city: Optional[str]
    customer_state: Optional[str]               #Optional[X] is equivalent to X | None (or Union[X, None]).

    #createdAt: datetime | None = None
    #updatedAt: datetime | None = None

    #@validator('customer_zip_code_prefix')
    #def prevent_none(cls, v):
    #    assert v is not None, 'customer_zip_code_prefix may not be None'
    #    return v


class CustomerCreate(CustomerBase):
    customer_zip_code_prefix: constr(min_length=1, max_length=10) #type method for constraining strs
    customer_city: constr(min_length=1, max_length=50)
    customer_state: constr(min_length=1, max_length=5)


class Customer(CustomerCreate):


    class Config:                                   #the Config class tells Pydantic to map the models to ORM objects. This is required since we’re using SQLAlchemy ORM in the project
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        #json_encoders = {customer_id: str, customer_unique_id: str, }
        json_schema_extra = {
            "example": {
                "customer_id": "Jane Doe",
                "customer_unique_id": "jdoe@example.com",
                "customer_zip_code_prefix": "Experiments, Science, and Fashion in Nanophotonics",
                "customer_city": "3.0",
                "customer_state": "3.0"
            }
        }

