from fastapi import APIRouter
from services.rick_morty_service import (
    fetch_characters,
    fetch_dead_characters,
    fetch_character_appearances_count
)

router = APIRouter(prefix="/characters", tags=["Characters"])


@router.get("/")
def get_characters():
    return fetch_characters()

@router.get("/dead")
def get_dead_characters():
    return fetch_dead_characters()

@router.get("/appearances/{character_name}")
def get_character_appearances_count(character_name: str):
    return fetch_character_appearances_count(character_name)