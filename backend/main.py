from fastapi import FastAPI
from routes.characters import router as characters_router
from core.http_client import client

app = FastAPI()

app.include_router(characters_router)


@app.on_event("shutdown")
async def shutdown():
    await client.aclose()
