from fastapi import FastAPI, HTTPException
from app.database import db
import time

app = FastAPI(title="FastAPI MongoDB Practice")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI MongoDB Practice API"}

@app.get("/health")
async def health_check():
    if db.verify_connection():
        return {"status": "healthy", "database": "connected"}
    raise HTTPException(status_code=503, detail="Database connection failed")

@app.get("/practice")
async def practice_ops():
    collection = db.get_collection("practice_collection")
    
    # Insert
    test_doc = {"name": "FastAPI Refactor", "timestamp": time.time()}
    result = collection.insert_one(test_doc)
    
    # Read
    found_doc = collection.find_one({"_id": result.inserted_id})
    if found_doc:
        found_doc["_id"] = str(found_doc["_id"])
        
    return {
        "inserted_id": str(result.inserted_id),
        "document": found_doc,
        "total_count": collection.count_documents({})
    }
