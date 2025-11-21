from pydantic import BaseModel,EmailStr
from fastapi import FastAPI

app = FastAPI()


class Address(BaseModel):
  street_no:int
  city:str
  zip_code:str
  
class User_address(BaseModel):
  id:int
  name:str
  email:EmailStr
  addresses: list[Address]  

@app.get("/")
def main():
  return {"hello": "world"}


@app.post("/valid")
def data_valid(userdata: User_address):
  print(f"Userdata: {userdata}")
  return userdata