from pydantic import BaseModel,EmailStr,ValidationError,field_validator,validator
from fastapi import FastAPI

app = FastAPI()


class address(BaseModel):
  street:int
  city:str
  zip_code:str
 
class user_with_address(BaseModel):
  id:int
  name:str
  email:EmailStr
  addresses: list[address] 
  
  @field_validator("name")
  def name_value_handle(cls,v):
    if len(v)<2:
      raise ValidationError("Name must be at least 2 character long")
    return v
  
  
@app.get("/")
def hello():
  return {"hello": "world"}

@app.post("/chat")
def user_data(userdata:user_with_address):
  print(f"userdata: {userdata}")
  return userdata


