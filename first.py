import tkinter as tk

def add_task():
    task = entry.get()
    tasks.append(task)
    update_list()
    entry.delete(0, tk.END)

def delete_task():
    try:
        index = task_list.curselection()[0]
        del tasks[index]
        update_list()
    except IndexError:
        pass

def delete_all_tasks():
    tasks.clear()
    update_list()

def update_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

window = tk.Tk()
window.title("The To-Do List")

frame = tk.Frame(window)
frame.pack()

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_list = tk.Listbox(window, height=10, width=50)
task_list.pack()

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

delete_all_button = tk.Button(window, text="Delete All Tasks", command=delete_all_tasks)
delete_all_button.pack()

exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.pack()

tasks = ["Exercise", "Practice Coding", "Complete Assignment", "Shopping"]
update_list()

window.mainloop()