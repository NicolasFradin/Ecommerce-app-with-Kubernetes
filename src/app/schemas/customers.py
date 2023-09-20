from datetime import datetime
from typing import List
from pydantic import BaseModel
from uuid import UUID

class CustomerSchema(BaseModel):
    customer_id: UUID
    customer_unique_id: str | None = None
    customer_zip_code_prefix: str | None = None
    customer_city: str | None = None
    customer_state: str | None = None

    #createdAt: datetime | None = None
    #updatedAt: datetime | None = None

    class Config:                                   #the Config class tells Pydantic to map the models to ORM objects. This is required since we’re using SQLAlchemy ORM in the project
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

