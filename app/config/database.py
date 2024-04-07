from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseFactory:
    def __init__(self, connection_url):
        self.engine = create_engine(connection_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def get_session(self):
        return self.SessionLocal()

DATABASE_URL = os.getenv("DATABASE_URL")
database_factory = DatabaseFactory(DATABASE_URL)
database_factory.Base.metadata.create_all(bind=database_factory.engine)
