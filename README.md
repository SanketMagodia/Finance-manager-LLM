
# Smart Finance Manager using local Large Language model (no API or paid services needed)


## Demo
![alt text](https://github.com/SanketMagodia/Finance-manager-LLM/blob/master/images/1.png)
![alt text](https://github.com/SanketMagodia/Finance-manager-LLM/blob/master/images/2.png)
![alt text](https://github.com/SanketMagodia/Finance-manager-LLM/blob/master/images/3.png)
## Description

This project implements a personal A.I finance management system with the following features:

- Speech-to-text input using an external service Streamlit-mic-recorder
- Entity and price extraction using local Noether Hermes 2 LLM model powered with LangChain operations 
- Data storage and retrieval using MongoDB
- Transaction table visualization with Streamlit
- Monthly and yearly spending graphs using visualization Plotly
- One-month spending predictions using regression models trained with scikit-learn
- Tailored spending advice from the LLM model based on user queries
- API development using FastAPI for interaction between server and client














## Requirements
- Download the model from https://gpt4all.io/index.html
- change the paths.py and links.py as per need
- Python 3.x
- MongoDB server
- See serverReq.txt and clientReq.txt file in the server/ and client/ folders respectively for server-client-specific dependencies and setup instructions.
- Ensure you have the required dependencies 
just run 
```bash
pip install -r filename.txt
```

## Usage/Examples

### 1. If you want to use just API and build your own app:
```bash
git clone https://github.com/SanketMagodia/Finance-manager-LLM.git
```
### Run this to start the server
```bash
    uvicorn main:app --reload
```
###  Use these commands for API calls
``` bash
import requests

#login - it returns userid eg.{"id": str(id)}
url ="http://localhost:8000/login"
json_body = {
    'email': 'example@example.com',
    'password': 'hashed_password',
}

#edit specific entry - it returns success or failed eg. {"response": "success"}
url ="http://localhost:8000/edit"
json_body = {
    'documentId': '65e8b2b08546e17deaee9ec1',
    'item': "plane",
    'price': 15000
}

# sending text of user speach to be added to database - it returns success or failed eg. {"response": "success"}
url ="http://localhost:8000/command"
json_body = {
    'id': '65e8b2b08546e17deaee9ec1',
    'speach': "I had some fries for 5 dollars",
}

# request for data for specific user - returns json list of data/expenses
url ="http://localhost:8000/DataReq"
json_body = {
    'id': '65e8b2b08546e17deaee9ec1',
    
}
#returns response in string eg. {"response": response}
url ="http://localhost:8000/askme" 
json_body = {
    'id': '65e8b2b08546e17deaee9ec1',
    'speach': "where I can save money?",
}

response = requests.post(url, json=json_body)
response.json()
```
### 2. To Run streamlit client
``` bash
   streamlit run app.py
```






## App Usage
- Register to make new account to record your own data
- login to see your dashboard
- write questions in sidebar to get personalized answers by LLM model
- Press start recording to record your voice and stop recording to stop
- Tick show more rows to see all your purchases

## Contributing

Contributions are always welcome!
- Fork the repository.
- Create your feature branch (git checkout -b feature/new-feature).
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature/new-feature).
- Create a new Pull Request.

