from fastapi import FastAPI
from enum import Enum
from typing import Union
from pydantic import BaseModel
app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Student(BaseModel):
    name:str
    desc: Union[str, None]=None
    price: float
    tax: Union[float, None] = 0

students = []

@app.put("/student/{_id}")
async def create_student(_id: int, student: Student, q: Union[str, None]=None):
    res = {"id": _id, **student.model_dump()}
    if q:
        res.update({"q": q})
    students.append(res)
    return res

@app.get("/students")
async def get_students():
    return students

@app.get("/student/{_id}")
async def get_student(_id: int):
    for student in students:
        if student['id'] == _id:
            return student        
    return {"No item exits"}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item