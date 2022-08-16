from datetime import datetime

from pydantic import BaseModel

from .time_range import TimeRange


class AvailabilityBase(TimeRange, BaseModel):
    start: datetime
    end: datetime


class AvailabilityCreate(AvailabilityBase):
    pass


class Availability(AvailabilityBase):
    id: int

    class Config:
        orm_mode = True
