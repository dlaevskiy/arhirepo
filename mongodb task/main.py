from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.hub

postC = db.post

post_data = {
    "title": "Python and MongoDB",
    "content": "PyMongo is fun, you guys",
    "author": "Scott"
}

result = postC.insert_one(post_data)
print("One post: {0}".format(result.inserted_id))

bills_post = postC.find_one({"author": "Scott"})
print(bills_post)

update_from = {"title": "Python and MongoDB"}
update_to = {"$set":
    {
        "title": "Python and MongoDBiwe",
    }
}

postC.update(update_from, update_to)
bills_post = postC.find_one({"author": "Scott"})
print(bills_post)
