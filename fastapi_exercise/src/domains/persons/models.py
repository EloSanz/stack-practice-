from pydantic import BaseModel
from typing import List, ClassVar

class Person(BaseModel):
    first: str
    lastname: str
    age: int

    # In-memory mock database to simulate persistence
    _db: ClassVar[List["Person"]] = []

    def save(self) -> None:
        """
        Simulate saving the person to a database.
        """
        if self not in Person._db:
            Person._db.append(self)
