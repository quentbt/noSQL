from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection

# Création 
document = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

# Récupération
query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)

# Modification
query = {"name": "John Doe"}
update = {"$set": {"age": 31}}
result = collection.update_one(query, update)
print("Modified document count:", result.modified_count)

# suppression
query = {"name": "John Doe"}
result = collection.delete_one(query)
print("Deleted document count:", result.deleted_count)