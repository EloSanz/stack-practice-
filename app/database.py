import os
import time
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

class Database:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client.practice_db

    def get_collection(self, name: str):
        return self.db[name]

    def verify_connection(self):
        try:
            self.client.admin.command('ismaster')
            return True
        except ConnectionFailure:
            return False

db = Database()
