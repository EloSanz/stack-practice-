from fastapi import APIRouter
from services.rick_morty_service import (
    fetch_characters,
    fetch_dead_characters,
    fetch_character_appearances_count
)

router = APIRouter(prefix="/characters", tags=["Characters"])


@router.get("/")
async def get_characters():
    return await fetch_characters()

@router.get("/dead")
async def get_dead_characters():
    return await fetch_dead_characters()

@router.get("/appearances/{character_name}")
async def get_character_appearances_count(character_name: str):
    return await fetch_character_appearances_count(character_name)