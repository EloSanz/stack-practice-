from pydantic import BaseModel

class WeatherResponse(BaseModel):
    temperature: float
    windspeed: float
    weathercode: int
