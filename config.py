from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

username = "sneha"
password = "sneha@1436"   

encoded_password = quote_plus(password)

uri = f"mongodb+srv://{username}:{encoded_password}@snehacodes.c2oquxf.mongodb.net/SnehaCodes?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['SnehaCodes']
collection = db['users_data']
