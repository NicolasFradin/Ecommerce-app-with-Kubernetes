from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status, Response
import sqlalchemy
from sqlalchemy.orm import Session

from app.db.db import get_session
from app.models.customers import CustomerModel
from app.schemas.customers import Customer, CustomerCreate, CustomerUpdate
from app.services.customers import CustomerService, get_customer_service

from fastapi.logger import logger as fastAPI_logger
from pydantic.types import UUID

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Customer])
def list_customers(skip: int = 0, limit: int = 100, customer_service: CustomerService = Depends(get_customer_service)) -> List[CustomerModel]:
    customers = customer_service.list(skip=skip, limit=limit)
    return customers

@router.get("/{customer_id}", response_model=Customer)
def read_customer(customer_id: UUID, customer_service: CustomerService = Depends(get_customer_service)) -> Optional[CustomerModel]:
    customer = customer_service.get(customer_id)
    return customer

@router.delete(
    "/{customer_id}",
    status_code=204,        #With 204 the response must not have a body.
)
def delete_customer(customer_id: UUID, customer_service: CustomerService = Depends(get_customer_service)) -> None:
    customer_service.delete(customer_id)

@router.post(
    "/",
    response_model=Customer,
    status_code=201,
    responses={409: {"description": "Conflict Error"}},
)
def create_customer(customer: CustomerCreate, customer_service: CustomerService = Depends(get_customer_service)) -> CustomerModel:
    return customer_service.create(customer)

@router.patch(
    "/{customer_id}",
    response_model=Customer,
    status_code=200
)
def update_customer(customer_id: UUID, customer: CustomerUpdate, customer_service: CustomerService = Depends(get_customer_service)) -> CustomerModel:
    return customer_service.update(customer_id, customer)