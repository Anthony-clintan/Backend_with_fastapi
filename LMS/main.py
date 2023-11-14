from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Book (BaseModel):
    name: str
    price: float
    des: Union[str, None] = None

