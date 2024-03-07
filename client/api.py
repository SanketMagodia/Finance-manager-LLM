import requests
import json
import links
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)
def login(email: str, password: str):
    url = links.API_URL+"login"
    json_body = {
        'email': email,
        'password': password,
    }
    logging.info('sending login request')
    response = requests.post(url, json=json_body)
    logging.info('login response received : '+str(response.json()))
    return response.json()

def register(email: str, username:str, password: str):
    url = links.API_URL+"register"
    json_body = {
        'email': email,
        "username": username,
        'password': password,
    }
    logging.info('sending register request')
    response = requests.post(url, json=json_body)
    logging.info('register response received : '+str(response.json()))
    return response.json()

def edit(documentKey: str, item: str, price: int):
    url = links.API_URL+"edit"
    json_body = {
        'documentId': documentKey,
        'item': item,
        'price': price
    }
    logging.info('sending edit request')
    response = requests.post(url, json=json_body)
    logging.info('edit response received : '+str(response.json()))
    return response.json()

def speach(userId: str, speach: str):
    url = links.API_URL+"command"
    json_body = {
        'id': userId,
        'speach': speach,
    }
    logging.info('sending register request')
    response = requests.post(url, json=json_body)
    logging.info('speach response received : '+str(response.json()))
    return response.json()

def reqData(userId):
    url = links.API_URL+"DataReq"
    json_body = {
        'id': userId,
    }
    logging.info('sending userData request')
    response = requests.post(url, json=json_body)
    logging.info('userDate request response received : '+str(response.json()))
    return response.json()