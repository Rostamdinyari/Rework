from pymongo import MongoClient

# Establish a connection to the MongoDB server
client = MongoClient("mongodb+srv://rdinyarish:Rrosshir12345@cluster0.jqbyfjn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# Access the database
db = client["Rework"]

# Access the collection within the database
collection = db["mainPage"]
