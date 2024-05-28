import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class UserAccInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x799")
        self.root.title("User Account Information")

        self.setup_ui()

    def setup_ui(self):
        self.image_bg = Image.open("ADAMSON-1.jpg")
        self.photo_bg = ImageTk.PhotoImage(self.image_bg)
        self.bg_label = Label(self.root, image=self.photo_bg)
        self.bg_label.place(relwidth=1, relheight=1)

        frame = Frame(self.root, width=900, height=500, bg="light gray")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label = Label(self.root, text="User Account Information", font=('serif', 25, 'bold'), bg="white")
        label.place(x=165, y=130)

        # Move image_pfp to be inside the frame
        self.image_pfp = Image.open("no pfp.png")
        self.image_pfp = self.image_pfp.resize((100, 100))
        self.photo_pfp = ImageTk.PhotoImage(self.image_pfp)
        self.pfp_label = Label(frame, image=self.photo_pfp)
        self.pfp_label.place(relx=0.08, rely=0.2, anchor=CENTER)  # Adjusted position inside frame

        self.first_name_label = Label(self.root, text="First Name", font=(13), bg="light gray")
        self.first_name_label.place(relx=.26, rely=.39)
        self.first_name = Entry(self.root, bg="#FFFFFF")
        self.first_name.place(relx=.26, rely=.43)

        self.middle_name_label = Label(self.root, text="Middle Name", font=(13), bg="light gray")
        self.middle_name_label.place(relx=.38, rely=.39)
        self.middle_name = Entry(self.root, bg="#FFFFFF")
        self.middle_name.place(relx=.38, rely=.43)

        self.last_name_label = Label(self.root, text="Last Name", font=(13), bg="light gray")
        self.last_name_label.place(relx=.51, rely=.39)
        self.last_name = Entry(self.root, bg="#FFFFFF")
        self.last_name.place(relx=.51, rely=.43)

        self.suffix_label = Label(self.root, text="Suffix", font=(13), bg="light gray")
        self.suffix_label.place(relx=.64, rely=.39)
        self.suffix = Entry(self.root, bg="#FFFFFF")
        self.suffix.place(relx=.64, rely=.43)

        self.department_label = Label(self.root, text="Department", font=(20), bg="light gray")
        self.department_label.place(relx=.76, rely=.39)
        self.department = Entry(self.root, bg="#FFFFFF")
        self.department.place(relx=.76, rely=.43)

        self.designation_label = Label(self.root, text="Designation", font=(20), bg="light gray")
        self.designation_label.place(relx=.15, rely=.50)
        self.designation = Entry(self.root, bg="#FFFFFF", width=40)
        self.designation.place(relx=.15, rely=.55)

        self.username_label = Label(self.root, text="Username", font=(20), bg="light gray")
        self.username_label.place(relx=.38, rely=.50)
        self.username = Entry(self.root, bg="#FFFFFF", width=40)
        self.username.place(relx=.38, rely=.55)

        self.password_label = Label(self.root, text="Password", font=(20), bg="light gray")
        self.password_label.place(relx=.63, rely=.50)
        self.password = Entry(self.root, bg="#FFFFFF", width=40, show="*")
        self.password.place(relx=.63, rely=.55)

        self.confirm_password_label = Label(self.root, text="Confirm Password", font=(20), bg="light gray")
        self.confirm_password_label.place(relx=.15, rely=.61)
        self.confirm_password = Entry(self.root, bg="#FFFFFF", width=40, show="*")
        self.confirm_password.place(relx=.15, rely=.66)

        self.usertype_label = Label(self.root, text="User Type", font=(20), bg="light gray")
        self.usertype_label.place(relx=.38, rely=.60)

        self.usertype_var = tk.StringVar()
        self.usertype_var.set('Select')
        self.usertype_combo = ttk.Combobox(self.root, width=20, textvariable=self.usertype_var)
        self.usertype_combo['values'] = ('Admin', 'Accounting', 'HR')
        self.usertype_combo.place(relx=.38, rely=.66)

        self.userstatus_label = Label(self.root, text="User Status", font=(20), bg="light gray")
        self.userstatus_label.place(relx=.55, rely=.61)
        self.userstatus = Entry(self.root, bg="#FFFFFF", width=26)
        self.userstatus.place(relx=.55, rely=.66)

        self.employeenum_label = Label(self.root, text="Employee Number", font=(20), bg="light gray")
        self.employeenum_label.place(relx=.70, rely=.61)
        self.employeenum = Entry(self.root, bg="#FFFFFF", width=28)
        self.employeenum.place(relx=.70, rely=.66)

        self.update_button = Button(self.root, text="Save", bg="#3E64dA", font=("Arial", 16),
                                    fg="#FFFFFF", width=10, command=self.save_data_query)
        self.update_button.place(relx=.36, rely=.78, anchor=CENTER)

        self.delete_button = Button(self.root, text="Delete", bg="#FFDB58", font=("Arial", 16),
                                    fg="#000000", width=10, command=self.delete_data_query)
        self.delete_button.place(relx=.51, rely=.78, anchor=CENTER)

        self.cancel_button = Button(self.root, text="Cancel", bg="#FFFFFF", font=("Arial, 16"),
                                    fg="#000000", width=10, command=self.clear_fields)
        self.cancel_button.place(relx=.66, rely=.78, anchor=CENTER)

        self.quit_button = Button(self.root, text="Quit", bg="#FF6347", font=("Arial", 16),
                                  fg="#FFFFFF", width=10, command=self.root.quit)
        self.quit_button.place(relx=.81, rely=.78, anchor=CENTER)

    def save_data_query(self):
        data = [
            self.first_name.get(),
            self.middle_name.get(),
            self.last_name.get(),
            self.suffix.get(),
            self.department.get(),
            self.designation.get(),
            self.username.get(),
            self.password.get(),
            self.confirm_password.get(),
            self.usertype_var.get(),
            self.userstatus.get(),
            self.employeenum.get()
        ]

        con = sqlite3.connect("USER_ACC_INFO.db")
        save_data_query = """
        INSERT INTO user_acc_info_tbl (first_name, middle_name, last_name, suffix, department, 
        designation, username, password, confirm_password, usertype, user_status, employee_num) VALUES (?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?)"""
        con.execute(save_data_query, data)
        con.commit()
        con.close()
        tk.messagebox.showinfo("Data Saved", "Data has been saved to the database")

        self.clear_fields()

    def clear_fields(self):
        self.first_name.delete(0, "end")
        self.middle_name.delete(0, "end")
        self.last_name.delete(0, "end")
        self.suffix.delete(0, "end")
        self.department.delete(0, "end")
        self.designation.delete(0, "end")
        self.username.delete(0, "end")
        self.password.delete(0, "end")
        self.confirm_password.delete(0, "end")
        self.usertype_combo.set('Select')
        self.userstatus.delete(0, "end")
        self.employeenum.delete(0, "end")

    def delete_data_query(self):
        employee_num = self.employeenum.get()
        if not employee_num:
            tk.messagebox.showerror("Error", "Employee number is required to delete a record")
            return

        con = sqlite3.connect("USER_ACC_INFO.db")
        delete_data_query = "DELETE FROM user_acc_info_tbl WHERE employee_num = ?"
        cur = con.cursor()
        cur.execute(delete_data_query, (employee_num,))
        con.commit()
        con.close()

        if cur.rowcount == 0:
            tk.messagebox.showerror("Error", "No record found with the given employee number")
        else:
            tk.messagebox.showinfo("Data Deleted", "Record has been deleted from the database")
            self.clear_fields()

if __name__ == "__main__":
    window = Tk()
    app = UserAccInfoApp(window)
    window.mainloop()
