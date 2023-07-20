# Here is a to-do list manager.

def print_menu():
    print("To-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added to the list.")

def view_tasks(tasks):
    if not tasks:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['name']}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['name']}' marked as completed.")
    except (ValueError, IndexError):
        print("Invalid input or task number. Please try again.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['name']}' removed from the list.")
    except (ValueError, IndexError):
        print("Invalid input or task number. Please try again.")

def todo_list_manager():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list_manager()
