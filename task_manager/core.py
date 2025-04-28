import json
import os
from task_manager.logger import setup_logger
from task_manager.config import get_tasks_file_path

logger = setup_logger()
TASKS_FILE = get_tasks_file_path()

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {"id": task_id, "description": description, "priority": priority}
    tasks.append(task)
    save_tasks(tasks)
    logger.info(f"Added task: {task}")
    print(f"Task added with ID: {task_id}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Priority: {task['priority']}")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    logger.info(f"Deleted task with ID: {task_id}")
    print(f"Task with ID {task_id} deleted.")
