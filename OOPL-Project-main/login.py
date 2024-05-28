import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Dummy username and password for demonstration
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        # You can add code here to open another window or perform other actions upon successful login
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Creating main window
root = tk.Tk()
root.title("Login Page")


# Username Label and Entry
username_label = tk.Label(root, text="Username:", font=("Arial", 12), bg="white")
username_label.place(x=50, y=50)
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.place(x=150, y=50)

# Password Label and Entry
password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="white")
password_label.place(x=50, y=100)
password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.place(x=150, y=100)

# Login Button
login_button = tk.Button(root, text="Login", command=login, font=("Arial", 12), bg="blue", fg="white")
login_button.place(x=150, y=150)


root.geometry("400x200")
root.mainloop()
