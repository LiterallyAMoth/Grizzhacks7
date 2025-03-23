import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

FILE_NAME = "assignments.txt"

def log_assignment():
    name = assignment_txt.get()
    date = due_date_txt.get()
    time = due_time_txt.get()
    text = f"{name}. {date}. {time}."

    if name and date and time:
        assignment_list.insert(tk.END, text)
    else:
        messagebox.showwarning("Missing Information", "Please fill out all fields.")

def save_to_file():
    with open(FILE_NAME, "w") as file:
        for item in assignment_list.get(0, tk.END):
            file.write(item + "\n")

def delete_line():
    selected_indices = assignment_list.curselection()
    for index in reversed(selected_indices):
        assignment_list.delete(index)

def Load_list():
    with open(FILE_NAME, "r") as file:
        for line in file:
             assignment_list.insert(tk.END, line.strip())

root = tk.Tk()
root.title("")
root.geometry("500x350")

frame = ttk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")


assignment_label = ttk.Label(frame, text="Assignment Name").grid(row=0, column=0)

assignment_txt = ttk.Entry(frame)
assignment_txt.grid(row=1, column=0, padx=30, pady=20)


due_date_label = ttk.Label(frame, text="Due Date").grid(row=0, column=1)

due_date_txt = ttk.Entry(frame)
due_date_txt.grid(row=1, column=1)


due_time_label = ttk.Label(frame, text="Due Time").grid(row=0, column=2)

due_time_txt = ttk.Entry(frame)
due_time_txt.grid(row=1, column=2, padx=30)


add_button = ttk.Button(frame, text="ADD", command=log_assignment).grid(row=2, column=1, pady=20)

save_button = ttk.Button(frame, text="SAVE", command=save_to_file).grid(row=2, column=2)

delete_button = ttk.Button(frame, text="Delete", command=delete_line).grid(row=2, column=0)

assignment_list = tk.Listbox(frame)
assignment_list.grid(row=3, column=0, columnspan=3, pady=10, sticky="ew")

Load_list()

root.mainloop()