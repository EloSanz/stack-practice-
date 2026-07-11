from fastapi import Depends
from sqlalchemy.orm import Session
from src.infrastructure.database.db import SessionLocal
from src.domains.persons.repository import PersonInterface, PersonRepository
from src.domains.persons.services import PersonService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_person_repository(db: Session = Depends(get_db)) -> PersonInterface:
    return PersonRepository(db)

def get_person_service(
    repository: PersonInterface = Depends(get_person_repository)
) -> PersonService:
    return PersonService(repository)

