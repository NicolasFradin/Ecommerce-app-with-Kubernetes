from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status, Response
import sqlalchemy
from sqlalchemy.orm import Session

from app.db.db import get_session
from app.models.items import ItemModel
from app.schemas.items import Item, ItemCreate, ItemUpdate
from app.services.items import ItemService, get_item_service

from fastapi.logger import logger as fastAPI_logger
from pydantic.types import UUID

router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Item])
def list_items(skip: int = 0, limit: int = 100, item_service: ItemService = Depends(get_item_service)) -> List[ItemModel]:
    items = item_service.list(skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: UUID, item_service: ItemService = Depends(get_item_service)) -> Optional[ItemModel]:
    item = item_service.get(item_id)
    return item

@router.delete(
    "/{item_id}",
    status_code=204,        #With 204 the response must not have a body.
)
def delete_item(item_id: UUID, item_service: ItemService = Depends(get_item_service)) -> None:
    item_service.delete(item_id)


@router.post(
    "/",
    response_model=Item,
    status_code=201,
    responses={409: {"description": "Conflict Error"}},
)
def create_item(item: ItemCreate, item_service: ItemService = Depends(get_item_service)) -> ItemModel:
    return item_service.create(item)

@router.patch(
    "/{item_id}",
    response_model=Item,
    status_code=200
)
def update_item(item_id: UUID, item: ItemUpdate, item_service: ItemService = Depends(get_item_service)) -> ItemModel:
    return item_service.update(item_id, item)