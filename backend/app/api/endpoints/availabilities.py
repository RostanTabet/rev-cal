from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import deps
from core import schemas

router = APIRouter(prefix='/availabilities', tags=['availabilities'])


@router.get('/', response_model=schemas.Availability)
def list_availabilities(db: Session = Depends(deps.get_db)):
    ...


@router.post('/', response_model=schemas.Availability)
def create_availability(availability: schemas.AvailabilityCreate, db: Session = Depends(deps.get_db)):
    ...


@router.delete('/{availibility_id}')
def delete_availabilities(id: int, db: Session = Depends(deps.get_db)):
    ...
