from pydantic import BaseModel

from .time_range import TimeRange


class AvailabilityBase(TimeRange, BaseModel):
    pass


class AvailabilityCreate(AvailabilityBase):
    pass


class Availability(AvailabilityBase):
    id: int

    class Config:
        orm_mode = True
