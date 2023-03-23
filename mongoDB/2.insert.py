import pymongo


if __name__ == "__main__":
    
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client["Retailers"]
    collection = db["Stores"]

    # *inserting only one item in database 
    # dictionary = {'name': 'JC Tyres', 'location': 'Jamjodhpur'}
    # collection.insert_one(dictionary)

    # *inserting many items at a time in database 
    insertThese = [
        {"Name": "JC Tyres", "Location": "Jamjodhpur", "Contact":"Ashvinbhai"},
        {"Name": "Darshan Studio", "Location": "Jamjodhpur", "Contact":"Dipakbhai"},
        {"Name": "Manan Hospital", "Location": "Jamjodhpur", "Contact":"Nishaben"},
        {"Name": "Jyoti Collection", "Location": "Upleta", "Contact":"Ramu Kaka"}
    ]
    collection.insert_many(insertThese)