from fastapi import FastAPI

import endpoints
from core.database import engine, Base

# Initialize the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(endpoints.availabilities.router)
app.include_router(endpoints.reservations.router)
