from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import database_factory

class BaseRouter:
    def __init__(self, controller):
        self.router = APIRouter()
        self.controller = controller

    @property
    def db(self):
        return database_factory.get_session()
