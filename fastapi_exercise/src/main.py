from fastapi import FastAPI
from src.api.v1.persons import router as persons_router

app = FastAPI(
    title="Person Management API",
    description="FastAPI service organized in a clean and scalable directory structure.",
    version="1.0.0"
)

# Register routes
app.include_router(persons_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
