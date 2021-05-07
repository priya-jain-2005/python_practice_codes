"""
1. Install mongodb for windows.
2. Then install pymongo library, this library help us to connect t mongodb.(pip install pymongo)

"""
import pymongo

#client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# In above url : mongodb -> protocol, 127.0.0.1->ip, 27017->port
# Creating a db

###############################################################################################
'''
mydb = client['Employee']
# Adding collection to the Employee db
information = mydb.employee_information
record = {
    'firstname': 'priya',
    'lastname': 'jain',
    'Team': 'Tools',
    'age': 29,
    'gender': 'F'
    }

# information.insert_one(record)
records = [
    {
        'firstname': 'Nikhil',
        'lastname': 'jain',
        'Team': 'CD',
        'age': 24,
        'gender': 'M'
    },
    {
        'firstname': 'Rajeev',
        'lastname': 'Jain',
        'Team': 'Sr. Manager',
        'age': 59,
        'gender': 'M'
    },
    {
        'firstname': 'Sunita',
        'lastname': 'Jain',
        'age': 58,
        'gender': 'F'
    }
    ]
'''
# information.insert_many(records)
# print(information.find_one({"age":58}))
# print(information.find())
'''
for record in information.find():
    print(record)
'''
'''
for record in information.find({'firstname': {'$in': ['Nikhil', 'priya']}}):
    print(record)
'''
'''
for record in information.find({'age': {'$gt': 50}}):
    print(record)
'''
# AND operator
'''
for record in information.find({'gender':'F', 'age': {'$lt': 50}}):
    print(record)
'''
# OR operator
'''
for record in information.find({'$or': [{'age': {'$gt': 50}}, {'firstname': 'Nikhil'}]}):
    print(record)
'''
'''
for record in information.find({'$and': [{'age': {'$gt': 50}}, {'firstname': 'Rajeev'}]}):
    print(record)
'''
############################################################################################################
# UPDATING RECORDS : update_one(),update_many(), replace_one()
# inventory = mydb.inventory
'''
inventory.insert_many([
    {"item": "canvas",
     "qty": 100,
     "size": {"h": 28, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "journal",
     "qty": 25,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "mat",
     "qty": 85,
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "mousepad",
     "qty": 25,
     "size": {"h": 19, "w": 22.85, "uom": "cm"},
     "status": "P"},
    {"item": "notebook",
     "qty": 50,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "P"},
    {"item": "paper",
     "qty": 100,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": {"h": 22.85, "w": 30, "uom": "cm"},
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": {"h": 10, "w": 15.25, "uom": "cm"},
     "status": "A"},
    {"item": "sketchbook",
     "qty": 80,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "sketch pad",
     "qty": 95,
     "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
     "status": "A"}])
'''
'''
inventory.update_one(
    {"item": "sketch pad"},
    {"$set": {"size.uom": "m", "status": "P"},
     "$currentDate": {"lastModified": True}}
)
'''
'''
inventory.update_many(
    {"qty": {"$lt": 50}},
    {"$set": {"size.uom": "m", "status": "P"},
     "$currentDate": {"lastModified": True}}
)
'''
'''
inventory.replace_one(
    {"item": "paper"},
    {
        "item": "paper",
        "instock": [
            {"warehouse": "A", "qty": 60},
            {"warehouse": "B", "qty": 76}
        ]

    }
)
'''
#######################################################################################################
# $sum, $avg, $project, $group
# Access database
'''
mydb2 = client["Students"]

# Access collection of the database
collections = mydb2["studentScores"]

data = [
    {"user": "Krish", "subject": "Database", "score": 80},
    {"user": "Amit",  "subject": "JavaScript", "score": 90},
    {"user": "Amit",  "title": "Database", "score": 85},
    {"user": "Krish",  "title": "JavaScript", "score": 75},
    {"user": "Amit",  "title": "Data Science", "score": 60},
    {"user": "Krish",  "title": "Data Science", "score": 95}]
'''
# collections.insert_many(data)
# Find Amit and Krish Total Subjects
'''
agg_result = collections.aggregate([{
    "$group": {
        "_id": "$user",
        "Total Subjects": {"$sum": 1}           # Counting no. of rows w.r.t. user field
        # when $sum:2 then Total Subjects: 6
        # when $sum:3 then Total Subjects: 9
    }
}])

for i in agg_result:
    print(i)
'''
# Total score based on user
'''
agg_result = collections.aggregate([{
    "$group": {
        "_id": "$user",
        "Total Marks": {"$sum": "$score"}
    }
}])
for i in agg_result:
    print(i)
'''

# Avg Score based on user
'''
agg_result = collections.aggregate([{
    "$group": {
        "_id": "$user",
        "StudentAvgScore": {"$avg": "$score" }
    }
}])

for i in  agg_result:
    print(i)
'''
###########################################################################################
'''
import datetime as datetime

data = [{"_id": 1, "item": "abc", "price": 10, "quantity": 2, "date": datetime.datetime.utcnow()},
        {"_id": 2, "item": "jkl", "price": 20, "quantity": 1, "date": datetime.datetime.utcnow()},
        {"_id": 3, "item": "xyz", "price": 5, "quantity": 5, "date": datetime.datetime.utcnow()},
        {"_id": 4, "item": "abc", "price": 10, "quantity": 10, "date": datetime.datetime.utcnow()},
        {"_id": 5, "item": "xyz", "price": 5, "quantity": 10, "date": datetime.datetime.utcnow()}]
mydb3 = client["Stores"]
mycollection = mydb3.myStore
# mycollection.insert_many(data)

# calculating avg price and avg quantity
agg_result = mycollection.aggregate([{
    "$group": {
        "_id": "$item",
        "average quantity": {"$avg": "$quantity"},
        "average price": {"$avg": {"$multiply": ["$price","$quantity"]}}
    }
}])
for i in agg_result:
    print(i)
'''
#######################################################################################
'''
mydb4 = client["Books"]
collection = mydb4.booksCollection
data = [{
  "_id": 1,
  "title": "abc123",
  "isbn": "0001122223334",
  "author": {"last": "zzz", "first": "aaa"},
  "copies": 5
},
    {
  "_id": 2,
  "title": "Baked Goods",
  "isbn": "9999999999999",
  "author": {"last": "xyz", "first": "abc", "middle": ""},
  "copies": 2
}]
# collection.insert_many(data)
# Demonstrating $project (similar to select statement in mysql)

for row in collection.aggregate([{"$project": {"title": 1, "isbn": 1}}]):
    print(row)
'''

###############################################################################
# Deleting database
'''
client.drop_database("Employee")
client.drop_database("Books")
client.drop_database("Stores")
client.drop_database("Students")
'''
############################################################################
# Connecting with Mongo db as service - mongo atlas
'''
import ssl
client = pymongo.MongoClient('mongodb+srv://mydbatlas:mydbatlas@cluster0.88yd1.mongodb.net/test', ssl_cert_reqs=
                             ssl.CERT_NONE)

mydb4 = client["Books"]
collection = mydb4.booksCollection
data = [{
  "_id": 1,
  "title": "abc123",
  "isbn": "0001122223334",
  "author": {"last": "zzz", "first": "aaa"},
  "copies": 5
},
    {
  "_id": 2,
  "title": "Baked Goods",
  "isbn": "9999999999999",
  "author": {"last": "xyz", "first": "abc", "middle": ""},
  "copies": 2
}]
collection.insert_many(data)
'''