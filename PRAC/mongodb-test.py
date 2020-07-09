import pymongo
from pymongo import MongoClient
import json

myclient = MongoClient("mongodb+srv://test:test@helloworld-cluster-mongodb-jrnrm.azure.mongodb.net/bolscraper?retryWrites=true&w=majority")
mydb = myclient["bolscraper"]
mycol = mydb["categories"]

test_arr = []

with open('bol_categories.json') as json_file:
    data = json.load(json_file)
    for sub_cat in data:
        for cat in sub_cat['sub_categories']:
            mydict = cat
            x = mycol.insert_one(mydict)

