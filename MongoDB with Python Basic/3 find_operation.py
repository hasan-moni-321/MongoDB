import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['mydatabase']
mycol = mydb['customers']

# Use of find_one
x = mycol.find_one()
print(x)


# Use of find_all
for x in mycol.find():
    print(x)


# Return Only Some Fields
for x in mycol.find({}, {'_id':0, "name":1, 'address':1}):
    print(x)

# This example will exclude "address" from the result
print("###########Printing all without address##############")
for x in mycol.find({}, {"address": 0}):
    print(x)


# Filter the Result
print("###########Finding query of a specific address############")
my_query = {"address": "Green Grass 1"}
mydoc = mycol.find(my_query)

for x in mydoc:
    print(x)

# Advance filter the result
print("#########Advance filtering###########3")
my_query = {"address": {"$gt": "S"}}
mydoc = mycol.find(my_query)

for x in mydoc:
    print(x)


# Filter With Regular Expressions
print("#######Using regular expression##########3")
myquery = {"address": {"$regex": "^S"}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

