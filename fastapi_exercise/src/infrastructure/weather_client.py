from dataclasses import dataclass, field
import httpx

@dataclass
class WeatherClient:
    client: httpx.Client = field(default_factory=lambda: httpx.Client(timeout=5.0))
    def get_current_weather(self, lat: float, lon: float) -> dict:
        """
        Clean HTTP client to fetch the current weather from Open-Meteo.
        Does not contain any retry/resilience logic.
        """
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,weather_code"
        response = self.client.get(url)
        response.raise_for_status()
        data = response.json()
        current = data.get("current", {})
        return {
            "temperature": current.get("temperature_2m"),
            "windspeed": current.get("wind_speed_10m"),
            "weathercode": current.get("weather_code")
        }
