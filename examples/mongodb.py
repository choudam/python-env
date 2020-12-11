# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:16:43 2020

@author: srinic
"""

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")


mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict={"name":"Srinivas", "address":"3613"}
x=mycol.insert_one(mydict)
mydict={"name":"Rao", "address":"3720"}
x=mycol.insert_one(mydict)
print(x.inserted_id)

print(myclient.list_database_names())
print(mydb.list_collection_names())


mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

try:
    x= mycol.insert_many(mylist)
    print(x.inserted_ids)
except:
    print("Duplicate records are not allowed")
      


x= mycol.find_one()

print(x)

print("All records")

[print(x) for x in mycol.find().sort("name")]


query={"name":"Rao"}
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(query,newvalues)

print("Print records for {1}", query)

[print(x) for x in mycol.find(query)]

mycol.delete_many(query)

[print(x) for x in mycol.find()]

mycol.drop()


