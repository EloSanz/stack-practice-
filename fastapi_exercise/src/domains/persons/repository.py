from abc import ABC, abstractmethod
from typing import List, cast
from sqlalchemy.orm import Session
from src.infrastructure.database.models import PersonDB, AddressDB
from .models import Person, Address

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
    def __init__(self, db: Session):
        self.db = db

    def savePerson(self, person: Person) -> None:
        """
        Save person and address into Postgres via SQLAlchemy.
        """
        db_address = AddressDB(
            street_name=person.address.street_name,
            street_number=person.address.street_number,
            lat=person.address.lat,
            long=person.address.long
        )
        self.db.add(db_address)
        self.db.flush()

        db_person = PersonDB(
            first=person.first,
            lastname=person.lastname,
            age=person.age,
            address_id=cast(int, db_address.id)
        )
        self.db.add(db_person)
        self.db.commit()

    def getAll(self) -> List[Person]:
        """
        Retrieve all persons and map them back to domain models.
        """
        db_persons = self.db.query(PersonDB).all()
        return [
            Person(
                first=cast(str, p.first),
                lastname=cast(str, p.lastname),
                age=cast(int, p.age),
                address=Address(
                    street_name=cast(str, p.address.street_name),
                    street_number=cast(int, p.address.street_number),
                    lat=cast(int, p.address.lat),
                    long=cast(int, p.address.long)
                )
            )
            for p in db_persons
        ]
