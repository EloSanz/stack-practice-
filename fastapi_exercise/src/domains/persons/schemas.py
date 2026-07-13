from pydantic import BaseModel, Field

class AddressCreateRequest(BaseModel):
    street_name: str = Field(..., min_length=2, max_length=100, description="Name of the street")
    street_number: int = Field(..., gt=0, description="Street number, must be positive")
    lat: int = Field(..., description="Latitude coordinate")
    long: int = Field(..., description="Longitude coordinate")

class PersonCreateRequest(BaseModel):
    first: str = Field(..., min_length=2, max_length=50, description="First name")
    lastname: str = Field(..., min_length=2, max_length=50, description="Last name")
    age: int = Field(..., gt=0, lt=130, description="Age, must be between 1 and 130")
    address: AddressCreateRequest = Field(..., description="Address details")

class PersonInAddress(BaseModel):
    first: str
    lastname: str
    age: int

class AddressWithPeople(BaseModel):
    id: int
    street_name: str
    street_number: int
    lat: int
    long: int
    persons: list[PersonInAddress]
