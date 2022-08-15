from sqlalchemy import Column, DateTime, Integer, String

from ..database import Base


class Availabilities(Base):
    __tablename__ = 'availabilities'

    id = Column(Integer, primary_key=True)
    start = Column(DateTime)
    end = Column(DateTime)


class Reservations:
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    start = Column(DateTime)
    end = Column(DateTime)
    title = Column(String)
    email = Column(String)
