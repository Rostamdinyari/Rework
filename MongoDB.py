from pymongo import MongoClient
from dotenv import load_dotenv
import os

#Install the python-dotenv package if you haven't already:
#pip install python-dotenv

load_dotenv()

# Establish a connection to the MongoDB server
client = MongoClient(os.getenv("MONGODB_CONNECTION"))
# Access the database
db = client["Rework"]

# Access the collection within the database
collection = db["mainPage"]
