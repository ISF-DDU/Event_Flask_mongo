import pymongo
import json 

if __name__ == "__main__":
    
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # print(client)
    db = client["Retailers"]
    collection = db["Stores"]

    # !this will return only one object data 
    # one = collection.find_one()
    # print(one)

    # !this will return only one object data which matches the passed data
    # one = collection.find_one({'Contact': 'Ashvinbhai'})
    # print(one)

    # !Here we cannot print directly all the docs and 
    allDocs = collection.find({'Location': 'Jamjodhpur'})
    
    # print((list(allDocs))) 
    print(type(allDocs))

    for item in allDocs:
        print(item)
    
    # *output
    # JC Tyres
    # Darshan Studio
    # Manan Hospital

