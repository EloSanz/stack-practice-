from core.http_client import syncClient

RICK_MORTY_API = "https://rickandmortyapi.com/api/character"


def fetch_characters():
    response = syncClient.get(RICK_MORTY_API)
    response.raise_for_status()
    return response.json()


def fetch_dead_characters():
    data = fetch_characters()
    characters = data.get("results", [])

    return [
        char for char in characters
        if char.get("status") == "Dead"
    ]


def fetch_character_appearances_count(character_name: str):
    data = fetch_characters()
    characters = data.get("results", [])
    character = next(
        (char for char in characters if character_name.casefold() in char.get("name").casefold()),
        None
    )
    if character:
        return f"{character.get('name')}:{len(character.get('episode', []))}"
    return 0
