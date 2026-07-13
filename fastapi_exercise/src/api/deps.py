from src.domains.weather.services import WeatherService
from fastapi import Depends
from sqlmodel import Session
from src.core.db import engine
from src.domains.persons.repository import PersonInterface, PersonRepository
from src.domains.persons.services import PersonService

def get_db():
    with Session(engine) as session:
        yield session

def get_person_repository(db: Session = Depends(get_db)) -> PersonInterface:
    return PersonRepository(db)

def get_person_service(
    repository: PersonInterface = Depends(get_person_repository)
) -> PersonService:
    return PersonService(repository)

def get_weather_service() -> WeatherService:
    from src.infrastructure.resilient_weather_client import ResilientWeatherClient
    from src.domains.weather.services import WeatherService
    client = ResilientWeatherClient()
    return WeatherService(client)

