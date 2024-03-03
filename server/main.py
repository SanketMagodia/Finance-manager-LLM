import os
from fastapi import FastAPI
from pydantic import BaseModel
import gpt4all
MODELPATH = "C:/Users/magod/AppData/Local/nomic.ai/GPT4All/Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"

app = FastAPI()

class DataStructure(BaseModel):
    question:str
    

        
@app.post("/askme")
async def process_long_text(request: DataStructure):
    QA_input = {'question':request.question}
    model=gpt4all.GPT4All(MODELPATH)
    processed_text = model.generate(QA_input["question"])
    return {"processed_text": processed_text}