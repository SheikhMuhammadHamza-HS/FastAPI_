
from pydantic import BaseModel,ValidationError

class User(BaseModel):
  id:int
  name:str
  email: str
  age: int
  

# valid data
user1 = {"id": 1, "name":"Hamza", "email": "abc@gmail.com","age":20}
user = User(**user1)
print(user.model_dump())

try:
    invalid_data = User(id="21",name="sasas",email="abccc@gmail.com")
    print(invalid_data)
except ValidationError as e:
    print(f"e: {e}")
