#from Firebase import db
import RPi.GPIO as GPIO # type: ignore
import time
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# set up the gpio board
GPIO.setmode(GPIO.BOARD)

# initialize the pin variables
FILE_NAME = "assignments.txt"
buzzer = 16
ControlPin = [7, 11, 13, 15]
loop = True
current_time = datetime.now()
name = ""
date = ""
time = ""
def log_assignment():
    name = assignment_txt.get()
    date = due_date_txt.get()
    time = due_time_txt.get()
    text = f"{name} is due at {date} {time}"
    text = date + "-" + time

    if name and date and time:
        assignment_list.insert(tk.END, text)
    else:
        messagebox.showwarning("Missing Information", "Please fill out all fields.")
    name = ""
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
root.geometry("800x500")

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


date_list = []
with open("assignments.txt", "r") as file:
    for line in file:
        line = line.replace("-", "")
        year = line[0:4]
        month = line[4:6]
        day = line[6:8]
        hour = line[8:10]
        minute = line[10:12]
        date_list.append(datetime(int(year), int(month), int(day), int(hour), int(minute)))

now = datetime.now()

homework_time = min(date_list, key=lambda x: abs(x - now))

print(homework_time)


# gpio pin setup
GPIO.setup(buzzer, GPIO.OUT)
for pin in ControlPin:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,0)
seq = [ [1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1] ]


# turns the buzzer to the desired logic level
def Buzzer(state):
    GPIO.output(buzzer, state)





# turns the stepper motor function on
def StepperMotor():
    for i in range (2560):
            for fullstep in range (4):
                for pin in range (4):
                    GPIO.output(ControlPin[pin], seq[fullstep][pin])
                time.sleep(0.002)



while loop:
        Buzzer(1)
        Buzzer(0)
        StepperMotor()
        Buzzer(1)  
        Buzzer(0)  
        loop = False

        

        

# def on_snapshot(doc_snapshot, changes, read_time):
#     action = changes.document.data["action"]
#     if action == "arrive":
#         Buzzer(0)
#     time.sleep(5)
#     Buzzer(1)
#     time.sleep(0.005)
#     StepperMotor()
#     Buzzer(0)    
# doc_ref = db.collection("Oswald").document("Oswald")
# doc_watch = doc_ref.on_snapshot(on_snapshot)
