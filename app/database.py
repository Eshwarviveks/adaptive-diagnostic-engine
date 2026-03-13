from pymongo import MongoClient # type: ignore
import os
from dotenv import load_dotenv

load_dotenv(".env")   # force load .env file

MONGO_URI = os.getenv("MONGO_URI")

print("Mongo URI:", MONGO_URI)

client = MongoClient(MONGO_URI)

db = client["adaptive_test"]

questions_collection = db["questions"]
sessions_collection = db["sessions"]

print("MongoDB Connected Successfully!")