import os
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import gpt4all
import db
import paths
import llmPrompts

MODELPATH = paths.MODEL

app = FastAPI()

class DataStructure(BaseModel):
    question:str
class LoginCreds(BaseModel):
    email: EmailStr
    password: str
class CommandsStructure(BaseModel):
    id: str
    question: str

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
    id = db.login(LoginCreds.email, LoginCreds.password)
    if id:
        return{"id": str(id)}
    else:
        return{"id": "not found"}

@app.post("/command")
def command(UserQuestion : CommandsStructure):
    entities, prices = llmPrompts.text_to_EntityPrice(UserQuestion.question)
    db.addExpense(UserQuestion.id, entities, prices)
    return{"response": "success"}
    

    