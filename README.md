# Advanced CLI Task Manager

This project is a command-line task manager built with Python.

## Features
- Add tasks
- List tasks
- Delete tasks
- Environment variable for tasks file
- Logging actions
- Unit testing with mocking

## Running

```bash
python3 -m task_manager.cli add "My Task" 1
python3 -m task_manager.cli list
python3 -m task_manager.cli delete 1
cat logs/task_manager.log
