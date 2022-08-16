from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import deps
from core import schemas

router = APIRouter(prefix='/reservations', tags=['reservations'])


@router.post('/', response_model=schemas.Reservation)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(deps.get_db)):
    ...


@router.delete('/{reservation_id}')
def delete_reservation(id: int, db: Session = Depends(deps.get_db)):
    ...
