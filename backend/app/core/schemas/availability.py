from datetime import datetime

from pydantic import BaseModel


class AvailabilityBase(BaseModel):
    start: datetime
    end: datetime


class AvailabilityCreate(AvailabilityBase):
    pass


class Availability(AvailabilityBase):
    id: int

    class Config:
        orm_mode = True
