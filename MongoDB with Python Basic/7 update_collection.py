import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['mydatabase']
mycol = mydb['customers']


####################################################
# Update one
####################################################

# Replacing with a new query
myqury = {'address': "Valley 345"}
new_qury = {"$set": {"address": "Canny 234"}}

mycol.update_one(myqury, new_qury)

# printing after updating
for x in mycol.find():
    print(x)


##########################################
#Update Many
##########################################

myqury = {'address': {'$regex': "^S"}}
new_qury = {"$set": {'name': "Minnie"}}
x = mycol.update_many(myqury, new_qury)
print(x.modified_count, "documents updated")


