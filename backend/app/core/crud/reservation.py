from .base import CRUDBase
from .. import models, schemas


class CRUDReservation(CRUDBase[models.Reservation, schemas.ReservationCreate]):
    pass
