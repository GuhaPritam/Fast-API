from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import pymongo
from typing import List

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
    new_message = {
        "id": data.id,
        "name": data.name,
        "message": data.message
    }
    result = mycol.insert_one(new_message)
    return {"message": "Message added successfully", "id": str(result.inserted_id)}
