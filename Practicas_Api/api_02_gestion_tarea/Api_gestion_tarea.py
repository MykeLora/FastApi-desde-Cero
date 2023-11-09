from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False


tasks = []

@app.get('/tasks/')
async def list_tasks():
    return tasks

@app.post('/tasks')
async def create_task(task: Task):
    tasks.append(task)
    return task

@app.get('/tasks/{task_id}')
async def get_task(task_id: int = Path(...,title="ID de la tarea")):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tasks[task_id]

@app.put('/tasks/{task_id}')
async def update_task(task_id: int, update_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404,detail="Tarea no encontrada")
    
    tasks[task_id] = update_task
    return update_task

@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404,detail="Tarea no encontrada")
    
    deleted_task = tasks.pop(task_id)
    return deleted_task