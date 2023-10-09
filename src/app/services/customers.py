from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.customers import CustomerModel
from app.schemas.customers import Customer, CustomerCreate
from app.db.db import get_session

from app.services.base import BaseService

class CustomerService(BaseService[CustomerModel, Customer, CustomerCreate]):
    def __init__(self, db_session: Session):
        super(CustomerService, self).__init__(CustomerModel, db_session)        # It would be possible to write: super().__init__(CustomerModel, db_session)

    def link_customer(self): #unique customer service function not callable by other services
        return None

    #def create():
    #    return None          #In case the method of the base class is not sufficient we can overwrite it

def get_customer_service(db_session: Session = Depends(get_session)) -> CustomerService:
    return CustomerService(db_session)

