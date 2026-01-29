import os
from dotenv import load_dotenv
from core.http_client import client

load_dotenv()

RICK_MORTY_API = os.getenv("RICK_MORTY_API", "https://rickandmortyapi.com/api/character")


async def fetch_characters():
    response = await client.get(RICK_MORTY_API)
    response.raise_for_status()
    return response.json()


async def fetch_dead_characters():
    data = await fetch_characters()
    characters = data.get("results", [])

    return [
        char for char in characters
        if char.get("status") == "Dead"
    ]

async def fetch_character_appearances_count(character_name: str):
    data = await fetch_characters()
    characters = data.get("results", [])
    character = next(
        (char for char in characters if character_name.casefold() in char.get("name").casefold()),
        None
    )
    if character:
        return f"{character.get('name')}:{len(character.get('episode', []))}"
    return 0
