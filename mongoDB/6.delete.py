import pymongo


if __name__ == "__main__":
    
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Retailers"]
    collection = db["Stores"]

    # !Delete One 
    # rec = {"Contact": "Ramu Kaka"}
    # collection.delete_one(rec)

    # !Delete Many
    # rec = {"Contact": "Ramu Kaka"}
    # up = collection.delete_many(rec)
    # print(up.deleted_count)
    

