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

















# db.coll.distinct("name")
# db.coll.find({name: "Max", age: 32}).explain("executionStats") #// or "queryPlanner" or "allPlansExecution"
# db.coll.countDocuments({age: 32}) // alias for an aggregation pipeline - accurate count

# // Comparison
# db.coll.find({"year": {$gt: 1970}})
# db.coll.find({"year": {$gte: 1970}})
# db.coll.find({"year": {$lt: 1970}})
# db.coll.find({"year": {$lte: 1970}})
# db.coll.find({"year": {$ne: 1970}})
# db.coll.find({"year": {$in: [1958, 1959]}})
# db.coll.find({"year": {$nin: [1958, 1959]}})


"""
// Logical
db.coll.find({name:{$not: {$eq: "Max"}}})
db.coll.find({$or: [{"year" : 1958}, {"year" : 1959}]})
db.coll.find({$nor: [{price: 1.99}, {sale: true}]})

db.coll.find({
  $and: [
    {$or: [{qty: {$lt :10}}, {qty :{$gt: 50}}]},
    {$or: [{sale: true}, {price: {$lt: 5 }}]}
  ]
})



"""