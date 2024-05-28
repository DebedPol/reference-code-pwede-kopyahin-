import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# Function to open the registration window

def open_registration():
    os.system('python User_Account_Information.py')

# Function to handle login
def login():
    employee_num = employee_entry.get()
    password = password_entry.get()

    if not employee_num or not password:
        messagebox.showerror("Error", "Please enter both Employee Number and Password")
        return

    # Connecting to the database
    con = sqlite3.connect('USER_ACC_INFO.db')
    cur = con.cursor()

    query = "SELECT usertype FROM user_acc_info_tbl WHERE employee_num = ? AND password = ?"
    cur.execute(query, (employee_num, password))
    result = cur.fetchone()

    if result:
        usertype = result[0]
        if usertype == 'HR':
            os.system('python HR.py')
        elif usertype == 'Admin':
            os.system('python Admin.py')
        elif usertype == 'Accounting':
            os.system('python ACCOUNTING.py')
    else:
        messagebox.showerror("Error", "Invalid Employee Number or Password")

    con.close()

# Create the main window
root = tk.Tk()
root.geometry("800x400")
root.title("Login Page")

# Create and place the login widgets

title_label = tk.Label(root, text="HOMEPAGE | ", font=("Verdana", 30), fg="dark blue")
title_label.place(relx=1.0, y=20, anchor='ne')  # Adjusted position
title_label = tk.Label(root, text="LOG-IN OR REGISTER ", font=("Arial", 18), fg="dark blue")
title_label.place(x=300, y=110)

tk.Label(root, text="Employee Number:", font=("Verdana", 12), fg="dark blue").place(x=220, y=180)
employee_entry = tk.Entry(root)
employee_entry.place(x=400, y=180)


tk.Label(root, text="Password:", font=("Verdana", 12), fg="dark blue").place(x=220, y=220)
password_entry = tk.Entry(root, show="*")
password_entry.place(x=400, y=220)

login_button = tk.Button(root, text="Login", font=("Arial", 12), bg='sky blue', fg='dark blue', command=login)
login_button.place(x=300, y=260)


register_button = tk.Button(root, text="Register", font=("Arial", 12), bg='#CDD6DB', fg='dark blue', command=open_registration)
register_button.place(x=400, y=260)

root.mainloop()
