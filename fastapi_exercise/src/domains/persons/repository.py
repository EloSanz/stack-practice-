from abc import ABC, abstractmethod
from typing import List, cast
from sqlalchemy.orm import Session
from src.infrastructure.database.models import PersonDB, AddressDB
from .models import Person, Address
from .schemas import AddressWithPeople, PersonInAddress

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

    @abstractmethod
    def getAddressWithPeople(self, address_id: int) -> AddressWithPeople | None:
        """
        Retrieve an Address and all associated People.
        """
        pass

    @abstractmethod
    def getAddress(self, address_id: int) -> Address | None:
        """
        Retrieve a single Address without loading associated People.
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
            address_id=db_address.id
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
                first=p.first,
                lastname=p.lastname,
                age=p.age,
                address=Address(
                    street_name=p.address.street_name,
                    street_number=p.address.street_number,
                    lat=p.address.lat,
                    long=p.address.long
                )
            )
            for p in db_persons
        ]

    def getAddressWithPeople(self, address_id: int) -> AddressWithPeople | None:
        """
        Retrieve Address by ID and list all people living there.
        """
        db_address = self.db.query(AddressDB).filter(AddressDB.id == address_id).first()
        if not db_address:
            return None
        return AddressWithPeople(
            id=db_address.id,
            street_name=db_address.street_name,
            street_number=db_address.street_number,
            lat=db_address.lat,
            long=db_address.long,
            persons=[
                PersonInAddress(
                    first=p.first,
                    lastname=p.lastname,
                    age=p.age
                )
                for p in db_address.persons
            ]
        )

    def getAddress(self, address_id: int) -> Address | None:
        """
        Retrieve a single Address by ID (ignores persons relationship).
        """
        db_address = self.db.query(AddressDB).filter(AddressDB.id == address_id).first()
        if not db_address:
            return None
        return Address(
            street_name=db_address.street_name,
            street_number=db_address.street_number,
            lat=db_address.lat,
            long=db_address.long
        )
