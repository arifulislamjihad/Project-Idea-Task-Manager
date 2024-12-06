from task_manager import add_task, view_task, remove_task, search_task, update_task


while True:
    print("\n\nWelcome to Task Manager")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Search Task")
    print("5. Update Task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter task due date: ")
        add_task(title, description, due_date)
        print("Task added successfully.")
    elif choice == "2":
        view_task()
    elif choice == "3":
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == "4":
        query = input("Enter the search query: ")
        search_task(query)
    elif choice == "5":
        index = int(input("Enter the index of the task to update: "))
        update_task(index)
    elif choice == "6":
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
