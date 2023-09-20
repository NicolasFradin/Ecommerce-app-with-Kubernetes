from fastapi import APIRouter, Depends, HTTPException, status, Response
import sqlalchemy
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.models.customers import CustomerModel
from app.schemas.customers import CustomerSchema

from fastapi.logger import logger as fastAPI_logger
from uuid import UUID

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[CustomerSchema])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    #customers = crud.get_customers(db, skip=skip, limit=limit)
    customers = db.query(CustomerModel).offset(skip).limit(limit).all()
    return customers


@router.get("/{customer_id}", response_model=CustomerSchema)
def read_customers(customer_id: UUID, db: Session = Depends(get_db)):
    #db_customer = crud.get_customer(db, user_id=user_id)
    customer = db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).first()

    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
#
#
# @router.post("/customers/", response_model=schemas.Customer)
# def create_customer(customer: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_customer = crud.get_customer_by_email(db, email=customer.email)
#     if db_customerr:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_customer(db=db, customer=customer)

