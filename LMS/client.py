
from pymongo.mongo_client import MongoClient
import ssl

uri = "mongodb+srv://anthonyclintan007:Manobala18@mongodbfirstcluster.xdg70jq.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, ssl_cert_reqs=ssl.CERT_NONE)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
