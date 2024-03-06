import pymongo
from datetime import datetime
from bson import ObjectId


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

users_collection = db['user']



def register_user(username : str, password : str, email : str, name : str, Monthly_salary : int):
    user_data = {
        "username": username,
        "password": password,
        "email": email,
        "personal_data": {
            "name": name,
            "salary": Monthly_salary,
        },
        "purchases": {
            "item": [],
            "price": [],
            "dates": []
        }
    }
    user_id = users_collection.insert_one(user_data).inserted_id
    return user_id

def addExpense(user_id , items : list, prices : list):
    user_id = ObjectId(user_id)
    date = [str(datetime.now().date()) for i in range(len(items))]
    user = db.user.find_one({"_id": user_id})
    user['purchases']['item'].extend(items)
    user['purchases']['price'].extend(prices)
    user['purchases']['dates'].extend(date)
    db.user.update_one({"_id":user_id},{"$set": user},upsert = True)
    return True

def login(email : str, password : str):
    user = db.user.find_one({"email": email, "password": password})
    if user:
        return user['_id']
    else:
        return False