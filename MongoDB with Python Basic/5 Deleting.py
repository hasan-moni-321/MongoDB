import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['mydatabase']
mycol = mydb['customers']

# Delete one
myquery = {"address": "Mountain 21"}
mycol.delete_one(myquery)


# Delete Many Documents
myqury = {"address": {"$regex": "^S"}}
x = mycol.delete_many(myqury)
print(x.deleted_count, "documents deleted.")


# Delete All Documents in a Collection
x = mycol.delete_many({})
print(x.deleted_count, "documents deleted.")

