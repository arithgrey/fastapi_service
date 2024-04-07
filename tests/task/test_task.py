from fastapi.testclient import TestClient
from app.task.controllers.task_manager import Task, TaskCreate, TaskUpdate, TaskManager
from app.task.routers import router

client = TestClient(router)

# Simulamos algunos datos de tareas para usar en las pruebas
task_data_1 = {"id": 1, "title": "Tarea 1", "description": "Descripción de la tarea 1"}
task_data_2 = {"id": 2, "title": "Tarea 2", "description": "Descripción de la tarea 2"}

# Creamos una instancia de TaskManager para manipular las tareas en las pruebas
task_manager = TaskManager()
task_manager.tasks_db.append(Task(**task_data_1))
task_manager.tasks_db.append(Task(**task_data_2))

def test_get_tasks():
    response = client.get("/")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == len(task_manager.tasks_db)
    assert tasks[0]["title"] == task_manager.tasks_db[0].title
    assert tasks[1]["description"] == task_manager.tasks_db[1].description

def test_get_task():
    task_id = 1
    response = client.get(f"/{task_id}")
    assert response.status_code == 200
    task = response.json()
    assert task["id"] == task_id
    assert task["title"] == task_manager.get_task_by_id(task_id).title

def test_create_task():
    new_task_data = {"title": "Nueva Tarea", "description": "Descripción de la nueva tarea"}
    response = client.post("/", json=new_task_data)
    assert response.status_code == 200
    new_task = response.json()
    assert new_task["title"] == new_task_data["title"]
    assert new_task["description"] == new_task_data["description"]

    # Verificamos que la nueva tarea haya sido agregada al administrador de tareas
    assert any(task.title == new_task_data["title"] for task in task_manager.tasks_db)

def test_update_task():
    task_id = 1
    updated_task_data = {"title": "Tarea Actualizada", "description": "Descripción actualizada"}
    response = client.put(f"/{task_id}", json=updated_task_data)
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["title"] == updated_task_data["title"]
    assert updated_task["description"] == updated_task_data["description"]

    # Verificamos que la tarea haya sido actualizada en el administrador de tareas
    updated_task_manager = task_manager.get_task_by_id(task_id)
    assert updated_task_manager.title == updated_task_data["title"]
    assert updated_task_manager.description == updated_task_data["description"]

def test_delete_task():
    task_id = 1
    response = client.delete(f"/{task_id}")
    assert response.status_code == 200
    deleted_task = response.json()
    assert deleted_task["id"] == task_id

    # Verificamos que la tarea haya sido eliminada del administrador de tareas
    assert task_manager.get_task_by_id(task_id) is None
