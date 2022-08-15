from .base import CRUDBase
from .. import models, schemas


class CRUDAvailability(CRUDBase[models.Availability, schemas.AvailabilityCreate]):
    pass
