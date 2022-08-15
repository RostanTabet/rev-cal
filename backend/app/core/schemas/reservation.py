from datetime import datetime

from pydantic import BaseModel, EmailStr


class ReservationBase(BaseModel):
    start: datetime
    end: datetime
    title: str
    email: EmailStr


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int

    class Config:
        orm_mode = True
