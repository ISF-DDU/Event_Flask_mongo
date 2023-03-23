import pymongo


if __name__ == "__main__":
    
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Retailers"]
    collection = db["Stores"]

    prev = {"Contact": "Ramu Kaka"}
    nextt = {"$set": {"Location": "Ahemdabad"}}

    up = collection.update_one(prev, nextt)
    print(up.modified_count)

    # for item in collection:
    #     print(item)