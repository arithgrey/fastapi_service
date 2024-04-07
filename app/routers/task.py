
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.task import TaskController
from app import schemas
from app.schemas.task import TaskCreate
from app.config.database import database_factory


class TaskRouter:
    def __init__(self):
        self.router = APIRouter()
        self.controller = TaskController()

        @self.router.post("/tasks/")
        async def create_task(task_data: TaskCreate, db: Session = Depends(lambda: database_factory.get_session())):
            return await self.controller.create_task(db=db, task_data=task_data)  # Pasamos el argumento task_data


    def get_router(self):
        return self.router

task_router = TaskRouter()