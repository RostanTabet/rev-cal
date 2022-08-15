from sqlalchemy import Column, DateTime, Integer

from ..database import Base


class Availability(Base):
    __tablename__ = 'availabilities'

    id = Column(Integer, primary_key=True)
    start = Column(DateTime)
    end = Column(DateTime)
