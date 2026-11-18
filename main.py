from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional,List

app=FastAPI()

class Item(BaseModel):
    name:str
    price:float
    is_offer:Optional[bool]=None

fake_db=[]

@app.get("/items")
def get_items():
    return {
        "code":200,
        "message":"获取成功",
        "data":fake_db
    }

@app.post("/items")
def create_item(item:Item):
    return{
        "code":201,
        "message":"创建成功",
        "data":item
    }