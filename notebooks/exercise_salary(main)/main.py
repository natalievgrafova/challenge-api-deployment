from enum import Enum
from fastapi import FastAPI, Path
from pydantic import BaseModel, validator
from typing import Optional


app = FastAPI()

class Item(BaseModel):
    salary:int
    bonus :int
    taxes :int

    

salary_inv = {1:Item(salary = 2500, bonus = 200, taxes =400)}
salary_calc = {"salary":2500, "bonus":200, "taxes" :400}

@app.get("/")
async def root():
    return {"message": "Salary information"}

@app.get("/details/{item_id}")
def get_details(item_id:int = Path(description = "The id of the item", gt=0, lt=3)):
    return salary_inv[item_id]

@app.get("/info")
async def salary_info():
    return {"salary":"2500", "bonus":"200", "taxes" :"400" }

@app.post("/create/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in salary_inv:
        return {"Error": "Item already exists"}
    else: 
        salary_inv[item_id] =item

        return salary_inv[item_id]

@app.get("/net/{item_id}")
def salary_net(item_id:int):
    if item_id in salary_inv:
        return f"Net salary is: {salary_inv[item_id].salary +salary_inv[item_id].bonus -salary_inv[item_id].taxes}"

@app.get("/double/{number}")
def double_number(number): 
    try: 

        return 2*int(number)
    except: 
        return("Type an integer")





    



