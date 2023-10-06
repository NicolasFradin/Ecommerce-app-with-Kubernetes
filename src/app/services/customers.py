from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.customers import CustomerModel
from app.schemas.customers import CustomerSchema
from app.db.db import get_session

from app.services.base import BaseService

class CustomerService(BaseService[CustomerModel, CustomerSchema]):
    def __init__(self, db_session: Session):
        super(CustomerService, self).__init__(CustomerModel, db_session)        # It would be possible to write: super().__init__(CustomerModel, db_session)

def get_customer_service(db_session: Session = Depends(get_session)) -> CustomerService:
    return CustomerService(db_session)