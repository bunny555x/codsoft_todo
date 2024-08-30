import tkinter as tk
from tkinter import messagebox, simpledialog
import pickle

# Function to load tasks from a file
def load_tasks():
    try:
        with open('tasks.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)

# Function to add a task
def add_task():
    title = simpledialog.askstring("Task Title", "Enter task title:")
    if title:
        tasks.append({"title": title, "completed": False})
        update_task_list()

# Function to edit a task
def edit_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        new_title = simpledialog.askstring("Edit Task", "Enter new task title:")
        if new_title:
            tasks[task_index]["title"] = new_title
            update_task_list()

# Function to mark a task as completed
def toggle_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks[task_index]["completed"] = not tasks[task_index]["completed"]
        update_task_list()

# Function to delete a task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks.pop(task_index)
        update_task_list()

# Function to update the listbox display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "[Completed]" if task["completed"] else "[Active]"
        task_listbox.insert(tk.END, f"{task['title']} {status}")
    save_tasks(tasks)

# Initialize the main window
root = tk.Tk()
root.title("To-Do List App")

# Initialize the tasks list
tasks = load_tasks()

# Create UI elements
frame = tk.Frame(root)
frame.pack(pady=10)

task_listbox = tk.Listbox(frame, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack(pady=5)

toggle_button = tk.Button(root, text="Toggle Completed", command=toggle_task)
toggle_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Populate the task listbox
update_task_list()

# Start the Tkinter event loop
root.mainloop()
