import tkinter as tk
from tkinter import messagebox, simpledialog


# -----------------------------
# File handling
# -----------------------------

FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(" | ")

                if len(parts) == 2:
                    task = parts[0]
                    done = parts[1] == "1"
                    tasks.append([task, done])

    except FileNotFoundError:
        pass

    return tasks


def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task, done in tasks:
            done_flag = "1" if done else "0"
            file.write(f"{task} | {done_flag}\n")


# -----------------------------
# Task operations
# -----------------------------

def refresh_list():
    listbox.delete(0, tk.END)

    for i, (task, done) in enumerate(tasks, start=1):

        if done:
            status = "✓"
        else:
            status = "○"

        listbox.insert(tk.END, f"{i}. {status} {task}")


def add_task():
    task = entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    tasks.append([task, False])

    entry.delete(0, tk.END)

    save_tasks()
    refresh_list()


def delete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task to delete."
        )
        return

    index = selected[0]

    task_name = tasks[index][0]

    confirm = messagebox.askyesno(
        "Delete Task",
        f"Do you want to delete:\n\n{task_name}?"
    )

    if confirm:
        tasks.pop(index)

        save_tasks()
        refresh_list()


def complete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task."
        )
        return

    index = selected[0]

    # Change True to False or False to True
    tasks[index][1] = not tasks[index][1]

    save_tasks()
    refresh_list()

    # Select the same task again
    listbox.selection_set(index)


def edit_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task to edit."
        )
        return

    index = selected[0]

    old_task = tasks[index][0]

    new_task = simpledialog.askstring(
        "Edit Task",
        "Enter the new task:",
        initialvalue=old_task
    )

    if new_task is not None:

        new_task = new_task.strip()

        if new_task == "":
            messagebox.showwarning(
                "Warning",
                "Task cannot be empty."
            )
            return

        tasks[index][0] = new_task

        save_tasks()
        refresh_list()

        listbox.selection_set(index)


def clear_completed():
    global tasks

    tasks = [task for task in tasks if not task[1]]

    save_tasks()
    refresh_list()


# -----------------------------
# Main Window
# -----------------------------

window = tk.Tk()

window.title("My To-Do List")
window.geometry("500x600")
window.resizable(False, False)

# -----------------------------
# Heading
# -----------------------------

title_label = tk.Label(
    window,
    text="MY TO-DO LIST",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=20)


# -----------------------------
# Input area
# -----------------------------

input_frame = tk.Frame(window)

input_frame.pack(pady=10)


entry = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 14)
)

entry.grid(row=0, column=0, padx=5)


add_button = tk.Button(
    input_frame,
    text="ADD",
    width=8,
    font=("Arial", 11, "bold"),
    command=add_task
)

add_button.grid(row=0, column=1, padx=5)


# -----------------------------
# Task List
# -----------------------------

list_frame = tk.Frame(window)

list_frame.pack(pady=20)


scrollbar = tk.Scrollbar(list_frame)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


listbox = tk.Listbox(
    list_frame,
    width=48,
    height=15,
    font=("Arial", 13),
    yscrollcommand=scrollbar.set,
    selectmode=tk.SINGLE
)

listbox.pack(side=tk.LEFT)

scrollbar.config(command=listbox.yview)


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(window)

button_frame.pack(pady=10)


complete_button = tk.Button(
    button_frame,
    text="Complete / Undo",
    width=15,
    command=complete_task
)

complete_button.grid(row=0, column=0, padx=5, pady=5)


edit_button = tk.Button(
    button_frame,
    text="Edit Task",
    width=15,
    command=edit_task
)

edit_button.grid(row=0, column=1, padx=5, pady=5)


delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    width=15,
    command=delete_task
)

delete_button.grid(row=1, column=0, padx=5, pady=5)


clear_button = tk.Button(
    button_frame,
    text="Clear Completed",
    width=15,
    command=clear_completed
)

clear_button.grid(row=1, column=1, padx=5, pady=5)


# -----------------------------
# Instructions
# -----------------------------

instruction_label = tk.Label(
    window,
    text="Select a task from the list and use the buttons above.",
    font=("Arial", 9)
)

instruction_label.pack(pady=15)


# -----------------------------
# Load existing tasks
# -----------------------------

tasks = load_tasks()

refresh_list()


# -----------------------------
# Run application
# -----------------------------

window.mainloop()