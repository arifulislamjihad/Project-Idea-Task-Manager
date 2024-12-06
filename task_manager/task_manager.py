import json

# Path to store the tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from storage (e.g., a JSON file)."""
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
            # Ensure every task has a 'status' key
            for task in tasks:
                if 'status' not in task:
                    task['status'] = 'Pending'  # Default status if missing
            return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save tasks to storage (e.g., a JSON file)."""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, description, due_date):
    """Add a new task to the list."""
    tasks = load_tasks()
    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'status': 'Pending'  # Set the initial status as 'Pending'
    }
    tasks.append(task)
    save_tasks(tasks)

def view_task():
    """View all tasks with their statuses."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. Title: {task['title']}, Description: {task['description']}, "
                  f"Due Date: {task['due_date']}, Status: {task['status']}")

def update_task(index):
    """Update the status of a task to 'Completed'."""
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        if tasks[index - 1]['status'] == "Pending":
            tasks[index - 1]['status'] = "Completed"
            save_tasks(tasks)
            print(f"Task {index} status updated to 'Completed'.")
        else:
            print(f"Task {index} is already completed.")
    else:
        print("Invalid index.")

def remove_task(index):
    """Remove a task based on the index."""
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully.")
    else:
        print("Invalid index.")

def search_task(query):
    """Search for tasks that match the query."""
    tasks = load_tasks()
    found_tasks = [task for task in tasks if query.lower() in task['title'].lower() or query.lower() in task['description'].lower()]
    
    if found_tasks:
        print("\nSearch Results:")
        for i, task in enumerate(found_tasks, start=1):
            print(f"{i}. Title: {task['title']}, Description: {task['description']}, "
                  f"Due Date: {task['due_date']}, Status: {task['status']}")
    else:
        print("No tasks found matching the query.")
