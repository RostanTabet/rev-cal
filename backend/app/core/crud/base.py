from typing import Generic, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..database import Base

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    """CRUD object with default methods to Create, Read, Delete."""

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int) -> ModelType | None:
        # noinspection PyUnresolvedReferences
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session, *, skip: int | None = None, limit: int | None = None) -> list[ModelType]:
        query = db.query(self.model)
        query = query if skip is None else query.offset(skip)
        query = query if limit is None else query.limit(limit)
        return query.all()

    def create(self, db: Session, obj: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
