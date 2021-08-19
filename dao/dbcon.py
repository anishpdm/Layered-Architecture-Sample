import pymongo
import sys
sys.path.insert(1, '/Users/anish/Documents/layered')
from pojo.domain import selectedDomain
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase= client["Data"]
Collection_name =mydatabase["data_to_store"]

# print(selectedDomain())