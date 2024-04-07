from sqlalchemy.orm import Session
from app.models.task import Task 
from app.schemas.task import TaskCreate


class TaskController:
    async def create_task(self, db: Session, task_data: TaskCreate):
        task_dict = task_data.dict()
        task = Task(**task_dict)
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    def get_all_tasks(self, db: Session):
        return db.query(Task).all()

    def get_task(self, db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()

    def update_task(self, db: Session, task_id: int, task_data: dict):
        task = self.get_task(db, task_id)
        if task:
            for key, value in task_data.items():
                setattr(task, key, value)
            db.commit()
            db.refresh(task)
        return task

    def delete_task(self, db: Session, task_id: int):
        task = self.get_task(db, task_id)
        if task:
            db.delete(task)
            db.commit()
        return task
