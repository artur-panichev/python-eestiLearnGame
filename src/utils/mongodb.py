from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/");

db = client["eesti-learn"];
table = db["users"];

for x in table.find({"login": "artur"}):
    print(x)