from pymongo import MongoClient
from config.config import MONGO_DB_URI, MONGO_DB_NAME

client = MongoClient(MONGO_DB_URI)
db = client[MONGO_DB_NAME]
