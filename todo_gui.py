import tkinter as tk
from datetime import datetime
import pickle

TASKS_FILE = "tasks.pkl"

# Load tasks from file if available
try:
    with open(TASKS_FILE, "rb") as file:
        tasks = pickle.load(file)
except FileNotFoundError:
    tasks = {}

def add_task():
    task_name = entry_task.get()
    category = entry_category.get()
    description = entry_description.get()
    
    if task_name:
        tasks[task_name] = {"completed": False, "created_at": datetime.now(), "category": category, "description": description}
        update_tasks_list()
        entry_task.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_description.delete(0, tk.END)

def view_tasks():
    tasks_listbox.delete(0, tk.END)
    for task, task_info in tasks.items():
        status = "Completed" if task_info["completed"] else "Not Completed"
        created_at = task_info["created_at"].strftime("%Y-%m-%d %H:%M:%S")
        category = task_info.get("category", "Uncategorized")
        description = task_info.get("description", "No Description")
        tasks_listbox.insert(tk.END, f"{task} ({status}) - Created at: {created_at} - Category: {category} - Description: {description}")

def mark_completed():
    selected_task = tasks_listbox.get(tk.ACTIVE)
    print("Selected task:", selected_task)
    if selected_task:
        task_name = selected_task.split(" (")[0]
        if task_name in tasks:
            tasks[task_name]["completed"] = True
            update_tasks_list()
        else:
            print(f"Task '{task_name}' not found.")
            print("Current tasks:", tasks)

def delete_task():
    selected_task = tasks_listbox.get(tk.ACTIVE)
    print("Selected task:", selected_task)
    if selected_task:
        task_name = selected_task.split(" (")[0]
        if task_name in tasks:
            del tasks[task_name]
            update_tasks_list()
        else:
            print(f"Task '{task_name}' not found.")
            print("Current tasks:", tasks)

def save_tasks():
    with open(TASKS_FILE, "wb") as file:
        pickle.dump(tasks, file)

def update_tasks_list():
    view_tasks()
    save_tasks()

# GUI setup
root = tk.Tk()
root.title("To-Do List App")

# Entry for adding tasks
entry_task = tk.Entry(root, width=30)
entry_task.grid(row=0, column=0, padx=10, pady=10)

# Entry for adding categories
entry_category = tk.Entry(root, width=20)
entry_category.grid(row=0, column=1, padx=10, pady=10)
entry_category.insert(0, "Uncategorized")  # Default category

# Entry for adding descriptions
entry_description = tk.Entry(root, width=40)
entry_description.grid(row=0, column=2, padx=10, pady=10)

# Buttons
button_add = tk.Button(root, text="Add Task", command=add_task)
button_add.grid(row=0, column=3, padx=10, pady=10)

button_view = tk.Button(root, text="View Tasks", command=view_tasks)
button_view.grid(row=1, column=0, padx=10, pady=10)

button_completed = tk.Button(root, text="Mark Completed", command=mark_completed)
button_completed.grid(row=1, column=1, padx=10, pady=10)

button_delete = tk.Button(root, text="Delete Task", command=delete_task)
button_delete.grid(row=1, column=2, padx=10, pady=10)

# Listbox for displaying tasks
tasks_listbox = tk.Listbox(root, width=60, height=10)
tasks_listbox.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Load initial tasks into the listbox
view_tasks()

# Start the GUI loop
root.mainloop()
