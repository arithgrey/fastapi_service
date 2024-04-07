# server.py

from fastapi import FastAPI
from app.routers.task import task_router

app = FastAPI()
app.include_router(task_router.get_router(), prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
