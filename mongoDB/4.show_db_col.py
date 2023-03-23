import pymongo


if __name__ == "__main__":
    
    client = pymongo.MongoClient("mongodb://localhost:27017")
    
    allDatabase = client.list_database_names()
    # print(allDatabase['Retailers'])

    col = client['Retailers']
    # print(col.list_collection_names())