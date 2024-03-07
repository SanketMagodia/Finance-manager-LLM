import os
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import gpt4all
import db
import paths
import llmPrompts
import logging
logging.basicConfig(filename='server.log', level=logging.INFO)

MODELPATH = paths.MODEL

app = FastAPI()
class RegisterCreds(BaseModel):
    email:EmailStr
    username:str
    password:str
class DataStructure(BaseModel):
    question:str
class LoginCreds(BaseModel):
    email: EmailStr
    password: str
class CommandsStructure(BaseModel):
    id: str
    speach: str
class EditStructure(BaseModel):
    documentId: str
    item: str
    price: int
class request(BaseModel):
    id: str
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
        
@app.post("/askme")
async def process_long_text(request: DataStructure):
    model=gpt4all.GPT4All(MODELPATH)
    processed_text = model.generate(request.question)
    return {"processed_text": processed_text}

@app.post("/login")
def login(LoginCreds : LoginCreds):
    logging.info('Login request received')
    id = db.login(LoginCreds.email, LoginCreds.password)
    if id:
        logging.info('login Id received')
        return{"id": str(id)}
    else:
        logging.info('login Id not found')
        return{"id": "not found"}
@app.post("/register")
def login(RegisterCreds : RegisterCreds):
    logging.info('Register request received - U-'+str(RegisterCreds.username)+" E-"+str(RegisterCreds.email)+" P-"+str(RegisterCreds.password))
    id = db.register_user(RegisterCreds.username, RegisterCreds.password, RegisterCreds.email)
    if id:
        logging.info('Registeration successful')
        return{"id": str(id)}
    else:
        logging.info('Registeration failed')
        return{"id": "not found"}

@app.post("/command")
def command(UserSpeach : CommandsStructure):
    logging.info('Speach received - '+ UserSpeach.speach)
    entities, prices = llmPrompts.text_to_EntityPrice(UserSpeach.speach)
    if entities == []:
        logging.info('Failed to updated new expenses')
        return{"response": "failed"}
    if db.addExpense(UserSpeach.id, entities, prices):
        logging.info('database updated with new expenses')
        return{"response": "success"}
    else:
        logging.info('Failed to updated new expenses')
        return{"response": "failed"}
    
@app.post("/edit")
def edit(editInfo : EditStructure):
    logging.info('Edit request received')
    if db.edit(editInfo.documentId, editInfo.item, editInfo.price):
        logging.info('edit successful')
        return{"response": "success"}
    else:
        logging.info('edit failed')
        return{"response": "failed"}
    
@app.post("/DataReq")
def dataReq(UserId: request):
    logging.info('user data request received')
    docs = db.returnDocs(UserId.id)
    if docs:
        logging.info('user data pulled success')
        return docs
    else:
        logging.info('user data failed to pull')
        return {"response": "failed"}