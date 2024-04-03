from typing import Annotated
from fastapi import FastAPI, Path, Query,Body
from pydantic import BaseModel,Field,HttpUrl
from typing import Annotated


class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, examples=["A very nice Item"], max_length=300)        
    price: float = Field(
        examples=[35.4],gt=0, description="The price must be greater than zero")
    tax: float | None = Field(default=None, examples=[3.2])
    tags: set[str] = set()
    images: list[Image] | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]