from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
import certifi
ca = certifi.where()

uri = "mongodb+srv://anthonyclintan007:Manobala18@mongodbfirstcluster.xdg70jq.mongodb.net/?retryWrites=true&w=majority"
client = AsyncIOMotorClient(uri, tlsCAFile=ca)

# client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/test?retryWrites=true&w=majority")
db = client["lms"]
student_collection = db["students"]
