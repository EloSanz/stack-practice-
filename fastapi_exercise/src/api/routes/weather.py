from fastapi import APIRouter, Depends, HTTPException
from src.api.deps import get_person_service, get_weather_service
from src.domains.persons.services import PersonService
from src.domains.weather.services import WeatherService
from src.domains.weather.schemas import WeatherResponse

router = APIRouter(prefix="/weather", tags=["Weather"])

@router.get("/address/{address_id}", response_model=WeatherResponse)
def get_weather_for_address(
    address_id: int,
    person_service: PersonService = Depends(get_person_service),
    weather_service: WeatherService = Depends(get_weather_service)
):
    """
    Retrieve current weather for a specific address.
    Collaborates between PersonService (coordinates) and WeatherService (climatology).
    """
    address = person_service.get_address(address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    
    return weather_service.get_weather(address.lat, address.long)
