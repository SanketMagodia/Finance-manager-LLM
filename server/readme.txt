import requests
url ="http://localhost:8000/login"
json_body = {
    'email': 'example@example.com',
    'password': 'hashed_password',
}

url ="http://localhost:8000/edit"
json_body = {
    'documentId': '65e8b2b08546e17deaee9ec1',
    'item': "plane",
    'price': 15000
}
url ="http://localhost:8000/command"
json_body = {
    'id': '65e8b2b08546e17deaee9ec1',
    'speach': "I had some fries for 5 dollars",
}
url ="http://localhost:8000/DataReq"
json_body = {
    'id': '65e8b2b08546e17deaee9ec1',
}

response = requests.post(url, json=json_body)
response.json()