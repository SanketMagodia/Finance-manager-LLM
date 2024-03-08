import pymongo
from datetime import datetime
from bson import ObjectId
import json
import logging

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

users_collection = db['user']
purchases = db['purchases']


def register_user(username : str, password : str, email : str):
    logging.info('DB - registration request')
    user_data = {
        "username": username,
        "password": password,
        "email": email,
        "purchases": []
            
    }
    user_id = users_collection.insert_one(user_data).inserted_id
    logging.info('DB - user registered in db')
    return user_id

def addExpense(user_id : str , items : list, prices : list):
    logging.info('DB - Adding expenses')
    user_id = ObjectId(user_id)
    date = [str(datetime.now().date()) for i in range(len(items))]
    user = db.user.find_one({"_id": user_id})
    for i , j , k in zip(items, prices, date):
        PurchaseData = {"item": i,
            "price": j,
            "dates": k }
        purchase_Id = purchases.insert_one(PurchaseData).inserted_id
        user['purchases'].extend([purchase_Id])
        db.user.update_one({"_id":user_id},{"$set": user},upsert = True)
        logging.info('DB - adding '+str(i))
    logging.info('DB - expenses updated')
    return True

def login(email : str, password : str):
    user = db.user.find_one({"email": email, "password": password})

    if user:
        logging.info('DB - user Id found')
        return user['_id']
    else:
        logging.info('DB - user Id not found')
        return False
    
def edit(document_id :str, item :str, price: int):
    document_id = ObjectId(document_id)
    document = db.purchases.find_one({'_id':document_id})
    document['item'] = item
    document['price'] = price
    purchases.update_one({"_id": document_id}, {"$set": document})
    logging.info('DB - documents edited')
    return True

def returnDocs(userId : str):
    user = db.user.find_one({"_id": ObjectId(userId)})
    purchase_ids = user.get("purchases", [])
    purchase = list(purchases.find({"_id": {"$in": purchase_ids}}))
    for i in range(len(purchase)):
        purchase[i]["_id"]= str(purchase[i]["_id"])
    logging.info('DB - extracting user data')
    return json.dumps(purchase)