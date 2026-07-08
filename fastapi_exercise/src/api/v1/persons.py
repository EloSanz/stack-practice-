from fastapi import APIRouter, Depends
from typing import List
from src.domains.persons.models import Person
from src.domains.persons.services import PersonService
from src.api.deps import get_person_service

router = APIRouter(prefix="/persons", tags=["Persons"])

@router.post("", response_model=Person, status_code=201)
def add_person(
    person: Person,
    service: PersonService = Depends(get_person_service)
):
    """
    Endpoint to create and persist a Person.
    """
    service.save_person(person)
    return person

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
