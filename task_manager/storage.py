import json
import os

def save_task(tasks):
    with open('task.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def load_task():
    if not os.path.exists('task.json'):
        return []
    with open('task.json', 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
