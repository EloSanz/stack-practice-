from src.infrastructure.weather_client import WeatherClient
from .schemas import WeatherResponse

class WeatherService:
    def __init__(self, client: WeatherClient):
        self.client = client

    def get_weather(self, lat: float, lon: float) -> WeatherResponse:
        """
        Retrieves weather information from the client for specified coordinates.
        """
        data = self.client.get_current_weather(lat, lon)
        return WeatherResponse(**data)
