from fastapi import FastAPI
from db.database import create_db_and_tables
from contextlib import asynccontextmanager
from routes.characters import router as characters_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(characters_router)