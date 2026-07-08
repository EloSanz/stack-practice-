from fastapi import Depends
from src.domains.persons.repository import PersonInterface, PersonRepository
from src.domains.persons.services import PersonService

def get_person_repository() -> PersonInterface:
    return PersonRepository()

def get_person_service(
    repository: PersonInterface = Depends(get_person_repository)
) -> PersonService:
    return PersonService(repository)
