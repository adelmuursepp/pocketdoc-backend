import os
from pymongo import MongoClient

# MongoDB connection setup
def get_database():
    CONNECTION_STRING = f"mongodb+srv://{os.environ['USERNAME']}:{os.environ['PASSWORD']}@pocketdoccluster.dygbqiw.mongodb.net/pocketdocdb?retryWrites=true&w=majority&appName=pocketdoccluster"
    client = MongoClient(CONNECTION_STRING)
    return client["pocketdocdb"]