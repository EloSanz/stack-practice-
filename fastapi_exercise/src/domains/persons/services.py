from typing import List
from .models import Person
from .repository import PersonInterface

class PersonService:
    def __init__(self, repository: PersonInterface):
        self.repository = repository

    def save_person(self, person: Person) -> None:
        """
        Saves a person using the repository.
        """
        self.repository.savePerson(person)

    def list_people(self) -> List[Person]:
        """
        Retrieves the complete list of people.
        """
        return self.repository.getAll()

    def list_people_of_legal_age(self) -> List[Person]:
        """
        Retrieves the list of people who are of legal age (age >= 18).
        """
        return [person for person in self.repository.getAll() if person.age >= 18]
