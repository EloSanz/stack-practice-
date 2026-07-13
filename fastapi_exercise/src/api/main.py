from fastapi import APIRouter

from src.api.routes import persons, weather

api_router = APIRouter()
api_router.include_router(persons.router)
api_router.include_router(weather.router)
