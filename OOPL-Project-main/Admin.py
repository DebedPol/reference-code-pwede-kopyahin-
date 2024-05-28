import tkinter as tk
import os

def open_accounting():
    os.system('python ACCOUNTING.py')

def open_hr():
    os.system('python HR.py')

# Create the main window
root = tk.Tk()
root.geometry("750x300")
root.title("Welcome, Admin")

# Create and place the title label in the upper right corner
title_label = tk.Label(root, text="ADMIN PAGE ", font=("Arial", 30), fg="dark blue")
title_label.place(relx=1.0, y=20, anchor='ne')  # Adjusted position
title_label = tk.Label(root, text="Select Access |", font=("Arial", 18), fg="dark blue")
title_label.place(relx=1.0, y=65, anchor='ne')  # Adjusted position
# Create and place the Payroll button
payroll_button = tk.Button(root, text="             Payroll Access             ",font=("Arial", 12), bg='#CDD6DB', fg='dark blue', command=open_accounting)
payroll_button.place(x=280, y=170)

# Create and place the Employee Information button
employee_info_button = tk.Button(root, text="Employee Information Access", font=("Arial", 12), bg='#CDD6DB', fg='dark blue', command=open_hr)
employee_info_button.place(x=280, y=220)

root.mainloop()
