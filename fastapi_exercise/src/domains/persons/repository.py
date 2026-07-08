from abc import ABC, abstractmethod
from typing import List
from .models import Person

class PersonInterface(ABC):
    @abstractmethod
    def savePerson(self, person: Person) -> None:
        """
        Abstract method to save a Person object.
        """
        pass

    @abstractmethod
    def getAll(self) -> List[Person]:
        """
        Abstract method to retrieve all Person objects.
        """
        pass

class PersonRepository(PersonInterface):
    def savePerson(self, person: Person) -> None:
        """
        Implementation of saving a Person using Person.save().
        """
        person.save()

    def getAll(self) -> List[Person]:
        """
        Implementation of retrieving all Person objects.
        """
        return Person._db
