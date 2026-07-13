import logging
from tenacity import retry, stop_after_attempt, wait_exponential, before_sleep_log
from .weather_client import WeatherClient

logger = logging.getLogger(__name__)

class ResilientWeatherClient(WeatherClient):
    """
    Adapter/Proxy that adds retry capabilities to WeatherClient using Tenacity.
    """
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        reraise=True
    )
    def get_current_weather(self, lat: float, lon: float) -> dict:
        return super().get_current_weather(lat, lon)
