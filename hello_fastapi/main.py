from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessgeInput(BaseModel):
  role: str
  content: str
  
class chatInput(BaseModel):
  message: list[MessgeInput]

@app.get("/")
def hello_msg():
  return {"message": "Hellow hey"}

@app.post("/chat/start")
async def start_chat(data_received: chatInput):
  
  print(f"chat Input: {data_received.model_dump()}")
  print(f"chat Input type: {type(data_received.model_dump())}")
  print(f"chat Input type: {type(data_received)}")
  print(f"chat Message: {data_received.message}")
  print(f"chat Message type: {type(data_received.message)}")
  return data_received