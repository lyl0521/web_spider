import pymongo

db_client = pymongo.MongoClient()

db = db_client['db_douban']
db_collection = db['movie']

result1 = db_collection.find_one({"name":"霸王别姬"})
result2 = db_collection.find({})
result3 = db_collection.find({"director":"宫崎骏"})

print(result1)
for i in result3:
    print(i)

db_client.close()