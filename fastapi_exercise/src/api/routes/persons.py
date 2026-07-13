from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.domains.persons.models import Person, Address
from src.domains.persons.services import PersonService
from src.api.deps import get_person_service
from src.domains.persons.schemas import PersonCreateRequest, AddressWithPeople

router = APIRouter(prefix="/persons", tags=["Persons"])

@router.post("", response_model=Person, status_code=201)
def add_person(
    payload: PersonCreateRequest,
    service: PersonService = Depends(get_person_service)
):
    """
    Endpoint to create and persist a Person.
    """
    domain_person = Person(
        first=payload.first,
        lastname=payload.lastname,
        age=payload.age,
        address=Address(
            street_name=payload.address.street_name,
            street_number=payload.address.street_number,
            lat=payload.address.lat,
            long=payload.address.long
        )
    )
    service.save_person(domain_person)
    return domain_person

@router.get("/listPeople", response_model=List[Person])
def list_people(
    service: PersonService = Depends(get_person_service)
):
    """
    Endpoint that returns the list of all registered people.
    """
    return service.list_people()

@router.get("/listPeopleWithLegalAge", response_model=List[Person])
def list_people_with_legal_age(
    service: PersonService = Depends(get_person_service)
):
    """
    Endpoint that returns only registered people of legal age (age >= 18).
    """
    return service.list_people_of_legal_age()

@router.get("/address/{address_id}", response_model=AddressWithPeople)
def get_address_with_people(
    address_id: int,
    service: PersonService = Depends(get_person_service)
):
    """
    Endpoint to retrieve an address and all the people associated with it.
    """
    result = service.get_address_with_people(address_id)
    if not result:
        raise HTTPException(status_code=404, detail="Address not found")
    return result
