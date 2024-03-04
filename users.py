from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def users():
    return {"users": "user1, user2, user3"}