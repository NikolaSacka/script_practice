import pickle
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.pkl"

# Load tasks from file if available
try:
    with open(TASKS_FILE, "rb") as file:
        tasks = pickle.load(file)
except FileNotFoundError:
    tasks = {}

def show_menu():
    print("To-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task():
    task_name = input("Enter the task name: ")
    tasks[task_name] = {"completed": False, "created_at": datetime.now()}
    print("Task added successfully!")

def view_tasks():
    print("Tasks:")
    for task, task_info in tasks.items():
        status = "Completed" if task_info["completed"] else "Not Completed"
        created_at = task_info["created_at"].strftime("%Y-%m-%d %H:%M:%S")
        print(f"- {task} ({status}) - Created at: {created_at}")

def mark_completed():
    task_name = input("Enter the task name to mark as completed: ")
    if task_name in tasks:
        tasks[task_name]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Task not found.")

def save_tasks():
    with open(TASKS_FILE, "wb") as file:
        pickle.dump(tasks, file)
        print("Tasks saved to file.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            save_tasks()
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
def main():
    try:
        while True:
            show_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                mark_completed()
            elif choice == "4":
                save_tasks()
                print("Exiting the To-Do List App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user. Goodbye!")

if __name__ == "__main__":
    main()
