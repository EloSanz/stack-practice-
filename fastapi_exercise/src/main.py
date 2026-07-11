from fastapi import FastAPI
from src.api.v1.persons import router as persons_router
from src.infrastructure.database.db import engine, Base
from src.infrastructure.database import models  # noqa: F401
from src.domains.persons.exceptions import PersonDomainException, person_domain_exception_handler

# Auto create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Person Management API",
    description="FastAPI service organized in a clean and scalable directory structure.",
    version="1.0.0"
)

# Register routes
app.include_router(persons_router)
app.add_exception_handler(PersonDomainException, person_domain_exception_handler)

#uv run python -m src.main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
