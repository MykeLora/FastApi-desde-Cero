from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8080",  # Agrega aquí los dominios permitidos
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["Get"],  # Permitir todos los encabezados
)


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
    resultado = list(filter(lambda t:t.id == task_id,tasks))

    if(len(resultado)):
        return resultado[0]
    
    raise HTTPException(status_code=404,detail=f"La tarea con el id {task_id} no existe.")


@app.put('/tasks/{task_id}')
async def update_task(task_id: int, update_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404,detail="Tarea no encontrada")
    
    tasks[task_id] = update_task
    return update_task

@app.delete('/tasks/{task_id}')
async def eliminar_taks_por_id(task_id: int):

    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)

        return {'Mensaje':'La categoria ha sido eliminada satisfatoriamente.'}
    
    raise HTTPException(status_code=404, detail=f'La tarea con el ID {task_id} no existe.')