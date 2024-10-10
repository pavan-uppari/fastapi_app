"""
Mongodb connection and configuration
"""

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://mailforworkuse692:gYKt0yGrYllpDfqM@fastapiappcluster.3nux4.mongodb.net/?retryWrites=true&w=majority&appName=FastApiAppCluster&ssl=true"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.temp_db

# Item table
T_Item = db["Item"]
