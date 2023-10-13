from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.items import ItemModel
from app.schemas.items import Item, ItemCreate
from app.db.db import get_session

from app.services.base import BaseService

class ItemService(BaseService[ItemModel, Item, ItemCreate]):
    def __init__(self, db_session: Session):
        super(ItemService, self).__init__(ItemModel, db_session)        # It would be possible to write: super().__init__(ItemModel, db_session)

    def link_item(self): #unique customer service function not callable by other services
        return None

    #def create():
    #    return None          #In case the method of the base class is not sufficient we can overwrite it

def get_item_service(db_session: Session = Depends(get_session)) -> ItemService:
    return ItemService(db_session)

