import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['mydatabase']
mycol = mydb['customers']

# Sorting with name
mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)


# Sorting with descending order
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
    print(x)






