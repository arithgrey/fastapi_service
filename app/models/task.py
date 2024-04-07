# app/models/task.py

from sqlalchemy import Column, Integer, String
from app.config.database import database_factory
Base = database_factory.Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
