from typing import List
from .models import Person, Address
from .repository import PersonInterface
from .schemas import AddressWithPeople

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

    def get_address_with_people(self, address_id: int) -> AddressWithPeople | None:
        """
        Retrieves an address with all its residents.
        """
        return self.repository.getAddressWithPeople(address_id)

    def get_address(self, address_id: int) -> Address | None:
        """
        Retrieves a single address without residents.
        """
        return self.repository.getAddress(address_id)
