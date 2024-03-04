from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    
users = [User(id=1, name="John"), User(id=2, name="Doe"), User(id=3, name="Smith"),User(id=4, name="Doe")]


def search_user(id:int):
    user = filter(lambda x: x.id == id, users)
    try:
        return list(user)[0]
    except:
        return {"message": "User not found"}


@app.get("/view/")
async def read_users():
    return list(users)

@app.get("/user/{id}")
async def user(id: int):
    user = filter(lambda x: x.id == id, users)
    try:
        return list(user)[0]
    except:
        return {"message": "User not found"}
    
@app.post("/view/")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"message": "User already exists"}
    else:
        users.append(user)
        return user


@app.put("/user/")
async def user(user:User):

    found = False

    for index,saved_user in enumerate(users):
        if saved_user.id == user.id:
            users[index] = user
            found = True
            return user
    if not found:
        return {"message": "User not found"}