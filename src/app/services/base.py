from typing import Any, Generic, List, Optional, Type, TypeVar

import sqlalchemy
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from app.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseService(Generic[ModelType, SchemaType, CreateSchemaType]):        # Our BaseService class uses a generic type to define the type of data that the service can handle.
    def __init__(self, model: Type[ModelType], db_session: Session):
        self.model = model
        self.db_session = db_session

    def get(self, id: Any) -> Optional[ModelType]:
        obj: Optional[ModelType] = self.db_session.query(self.model).get(id)
        print(obj)
        if obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj

    def list(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        objs: List[ModelType] = self.db_session.query(self.model).offset(skip).limit(limit).all()
        return objs

    def delete(self, id: Any) -> None:
        db_obj = self.db_session.get(self.model, id)
        if db_obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        self.db_session.delete(db_obj)
        self.db_session.commit()

    def create(self, obj: CreateSchemaType) -> ModelType:
        db_obj: ModelType = self.model(**obj.dict())
        self.db_session.add(db_obj)
        try:
            self.db_session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            self.db_session.rollback()
            if "duplicate key" in str(e):
                raise HTTPException(status_code=409, detail="Conflict Error")
            else:
                raise e
        return db_obj

    def update(self, id: Any, obj: UpdateSchemaType) -> Optional[ModelType]:
        db_obj = self.get(id)
        for column, value in obj.dict(exclude_unset=True).items():
            setattr(db_obj, column, value)
        self.db_session.commit()
        return db_obj
