import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['mydataset']

#printing the inbuilt dataset name
print(myclient.list_database_names())

# list of the database
dataset_list = myclient.list_database_names()

if 'mydataset' in dataset_list:
    print("dataset is available on the database")

