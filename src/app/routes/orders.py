from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status, Response
import sqlalchemy
from sqlalchemy.orm import Session

from app.db.db import get_session
from app.models.orders import OrderModel
from app.schemas.orders import Order, OrderCreate, OrderUpdate
from app.services.orders import OrderService, get_order_service

from fastapi.logger import logger as fastAPI_logger
from pydantic.types import UUID

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Order])
def list_orders(skip: int = 0, limit: int = 100, order_service: OrderService = Depends(get_order_service)) -> List[OrderModel]:
    orders = order_service.list(skip=skip, limit=limit)
    return orders

@router.get("/{order_id}", response_model=Order)
def read_order(order_id: UUID, order_service: OrderService = Depends(get_order_service)) -> Optional[OrderModel]:
    order = order_service.get(order_id)
    return order

@router.delete(
    "/{order_id}",
    status_code=204,        #With 204 the response must not have a body.
)
def delete_order(order_id: UUID, order_service: OrderService = Depends(get_order_service)) -> None:
    order_service.delete(order_id)

@router.post(
    "/",
    response_model=Order,
    status_code=201,
    responses={409: {"description": "Conflict Error"}},
)
def create_order(order: OrderCreate, order_service: OrderService = Depends(get_order_service)) -> OrderModel:
    return order_service.create(order)

@router.patch(
    "/{order_id}",
    response_model=Order,
    status_code=200
)
def update_order(order_id: UUID, order: OrderUpdate, order_service: OrderService = Depends(get_order_service)) -> OrderModel:
    return order_service.update(order_id, order)