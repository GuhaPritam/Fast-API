from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["messages"]

print(mydb.list_collection_names())

app = FastAPI()


class Items(BaseModel):
    id: int
    name: str
    message: str


@app.get('/')
def get_messages():
    messages = list(mycol.find({},  {"_id": 0}))
    # for message in messages:
    #     message["_id"] = str(message["_id"])
    return messages


@app.post('/add_message/')
def post_message(data: Items):
    existing_message = mycol.find_one({"id": data.id})

    if existing_message:
        raise HTTPException(status_code=400, detail="Message with this ID already exists")

    new_message = {
        "id": data.id,
        "name": data.name,
        "message": data.message
    }
    result = mycol.insert_one(new_message)
    return {"message": "Message added successfully", "id": str(result.inserted_id)}
