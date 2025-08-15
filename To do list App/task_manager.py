import tkinter as tk
import json
import os

task_file = "tasks.json" #name of file where we save/load our tasks
tasks = [] #global python list that store tasks in memory, initially it is empty but later filled with json file

light_pink = "#FFB6C1"
soft_pink = "#FFDBE9"
cream_pink = "#FFE6EE"

#funtion to load tasks from json file

def load_tasks():
    if os.path.exists(task_file): #for checking if the file exists or not
        with open(task_file, "r") as file:
            loaded = json.load(file)
            tasks.extend(loaded)
            for task in tasks:
                task_Listbox.insert(tk.END, task)

# saving the tasks in json file

def save_tasks():
    with open(task_file, "w") as file:
        json.dump(tasks, file) #writes the python list in json format 
def add_tasks():
    task = task_entry.get()
    if task.strip(): #if there is empty string then -> false
        tasks.append(task)
        task_Listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END )
        save_tasks()

def delete_tasks():
    selected = task_Listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        task_Listbox.delete(index)
        save_tasks()

def update_tasks():
    selected = task_Listbox.curselection()
    new_task = task_entry.get()
    if selected and new_task.strip():
        index = selected[0]
        tasks[index] = new_task
        task_Listbox.delete(index)
        task_Listbox.insert(index, new_task)
        task_entry.delete(0, tk.END)
        save_tasks()




window = tk.Tk()
window.title("To do List")
window.geometry("700x400")
window.configure(bg = cream_pink)

task_entry = tk.Entry(
    window, 
    font = ("Comic Sans MS", 14),
    width = 30
)
task_entry.pack(pady = 10)

button_frame = tk.Frame(
    window,
    bg = cream_pink,
    
)
button_frame.pack()

add_button = tk.Button(
    button_frame,
    text = "Add Task",
    font = ("Comic Sans MS", 12),
    command = add_tasks,
    bg = light_pink

)
add_button.grid(row = 0, column = 0, padx = 5)

delete_button = tk.Button(
    button_frame,
    text = "Delete Task",
    font = ("Comic Sans MS", 12),
    command = delete_tasks,
    bg = light_pink
)

delete_button.grid(row = 0, column = 1,  padx=5)

update_button = tk.Button(
    button_frame, 
    text = "Update Task",
    font = ("Comic Sans MS", 12),
    command = update_tasks,
    bg = light_pink

)
update_button.grid(row = 0, column = 2, padx = 5)

task_Listbox = tk.Listbox(

    window, 
    font = ("Comic Sans MS", 12),
    width = 40,
    height= 15,
    bg = soft_pink
)
task_Listbox.pack(pady= 10)

load_tasks()
window.mainloop()

    
