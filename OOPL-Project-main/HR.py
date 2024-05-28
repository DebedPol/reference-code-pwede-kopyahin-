import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
def init_db():
    conn = sqlite3.connect('employee_info.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employee (
                first_name TEXT,
                middle_name TEXT,
                surname TEXT,
                suffix TEXT,
                date_of_birth TEXT,
                nationality TEXT,
                gender TEXT,
                civil_status TEXT,
                department TEXT,
                designation TEXT,
                employee_status TEXT,
                employee_number TEXT PRIMARY KEY,
                contact_number TEXT,
                email_address TEXT,
                other_social_media TEXT,
                social_media_account TEXT,
                address_line1 TEXT,
                address_line2 TEXT,
                baranggay TEXT,
                municipality TEXT,
                province TEXT,
                zip_code TEXT,
                country TEXT,
                picture_path TEXT)''')
    conn.commit()
    conn.close()

def save_data():
    conn = sqlite3.connect('employee_info.db')
    c = conn.cursor()
    c.execute(
        '''INSERT OR REPLACE INTO employee VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (firstnametxt.get("1.0", END).strip(),
         middle_nametxt.get("1.0", END).strip(),
         surnametxt.get("1.0", END).strip(),
         suffixtxt.get("1.0", END).strip(),
         date_of_birthtxt.get("1.0", END).strip(),
         nationalitytxt.get("1.0", END).strip(),
         gender_var.get(),
         civil_status_var.get(),
         departmenttxt.get("1.0", END).strip(),
         designationtxt.get("1.0", END).strip(),
         employee_statustxt.get("1.0", END).strip(),
         employee_numbertxt.get("1.0", END).strip(),
         contact_numbertxt.get("1.0", END).strip(),
         email_addresstxt.get("1.0", END).strip(),
         other_social_mediatxt.get("1.0", END).strip(),
         social_media_accounttxt.get("1.0", END).strip(),
         address_line1txt.get("1.0", END).strip(),
         address_line2txt.get("1.0", END).strip(),
         baranggaytxt.get("1.0", END).strip(),
         municipalittxt.get("1.0", END).strip(),
         provincetxt.get("1.0", END).strip(),
         zip_codetxt.get("1.0", END).strip(),
         countrytxt.get("1.0", END).strip(),
         picturepathtxt.get("1.0", END).strip()))
    messagebox.showinfo("Success", "Data saved successfully!")
    conn.commit()
    conn.close()


def search_data():
    conn = sqlite3.connect('employee_info.db')
    c = conn.cursor()
    employee_number = employee_numbertxt.get("1.0", END).strip()
    c.execute('SELECT * FROM employee WHERE employee_number=?', (employee_number,))
    data = c.fetchone()
    if data:
        firstnametxt.delete("1.0", END)
        firstnametxt.insert(END, data[0])

        middle_nametxt.delete("1.0", END)
        middle_nametxt.insert(END, data[1])

        surnametxt.delete("1.0", END)
        surnametxt.insert(END, data[2])

        suffixtxt.delete("1.0", END)
        suffixtxt.insert(END, data[3])

        date_of_birthtxt.delete("1.0", END)
        date_of_birthtxt.insert(END, data[4])

        nationalitytxt.delete("1.0", END)
        nationalitytxt.insert(END, data[5])

        gender_var.set(data[6])
        civil_status_var.set(data[7])

        departmenttxt.delete("1.0", END)
        departmenttxt.insert(END, data[8])

        designationtxt.delete("1.0", END)
        designationtxt.insert(END, data[9])

        employee_statustxt.delete("1.0", END)
        employee_statustxt.insert(END, data[10])

        employee_numbertxt.delete("1.0", END)
        employee_numbertxt.insert(END, data[11])

        contact_numbertxt.delete("1.0", END)
        contact_numbertxt.insert(END, data[12])

        email_addresstxt.delete("1.0", END)
        email_addresstxt.insert(END, data[13])

        other_social_mediatxt.delete("1.0", END)
        other_social_mediatxt.insert(END, data[14])

        social_media_accounttxt.delete("1.0", END)
        social_media_accounttxt.insert(END, data[15])

        address_line1txt.delete("1.0", END)
        address_line1txt.insert(END, data[16])

        address_line2txt.delete("1.0", END)
        address_line2txt.insert(END, data[17])

        baranggaytxt.delete("1.0", END)
        baranggaytxt.insert(END, data[18])

        municipalittxt.delete("1.0", END)
        municipalittxt.insert(END, data[19])

        provincetxt.delete("1.0", END)
        provincetxt.insert(END, data[20])

        zip_codetxt.delete("1.0", END)
        zip_codetxt.insert(END, data[21])

        countrytxt.delete("1.0", END)
        countrytxt.insert(END, data[22])

        picturepathtxt.delete("1.0", END)
        picturepathtxt.insert(END, data[23])
    else:
        messagebox.showinfo("Error", "Employee not found.")
    conn.close()
def clear_fields():
    # Clear all entry fields
    firstnametxt.delete("1.0", END)
    middle_nametxt.delete("1.0", END)
    surnametxt.delete("1.0", END)
    suffixtxt.delete("1.0", END)
    date_of_birthtxt.delete("1.0", END)
    nationalitytxt.delete("1.0", END)
    gender_var.set(' Select ')
    civil_status_var.set(' Single')
    departmenttxt.delete("1.0", END)
    designationtxt.delete("1.0", END)
    employee_statustxt.delete("1.0", END)
    employee_numbertxt.delete("1.0", END)
    contact_numbertxt.delete("1.0", END)
    email_addresstxt.delete("1.0", END)
    other_social_mediatxt.delete("1.0", END)
    social_media_accounttxt.delete("1.0", END)
    address_line1txt.delete("1.0", END)
    address_line2txt.delete("1.0", END)
    baranggaytxt.delete("1.0", END)
    municipalittxt.delete("1.0", END)
    provincetxt.delete("1.0", END)
    zip_codetxt.delete("1.0", END)
    countrytxt.delete("1.0", END)
    picturepathtxt.delete("1.0", END)
def update_data():
    conn = sqlite3.connect('employee_info.db')
    c = conn.cursor()
    c.execute('''UPDATE employee SET 
                first_name=?, middle_name=?, surname=?, suffix=?, date_of_birth=?, nationality=?, gender=?, 
                civil_status=?, department=?, designation=?, employee_status=?, contact_number=?, email_address=?, 
                other_social_media=?, social_media_account=?, address_line1=?, address_line2=?, baranggay=?, 
                municipality=?, province=?, zip_code=?, country=?, picture_path=?
                WHERE employee_number=?''',
              (firstnametxt.get("1.0", END).strip(), middle_nametxt.get("1.0", END).strip(),
               surnametxt.get("1.0", END).strip(), suffixtxt.get("1.0", END).strip(),
               date_of_birthtxt.get("1.0", END).strip(), nationalitytxt.get("1.0", END).strip(),
               gender_var.get(), civil_status_var.get(), departmenttxt.get("1.0", END).strip(),
               designationtxt.get("1.0", END).strip(), employee_statustxt.get("1.0", END).strip(),
               contact_numbertxt.get("1.0", END).strip(), email_addresstxt.get("1.0", END).strip(),
               other_social_mediatxt.get("1.0", END).strip(), social_media_accounttxt.get("1.0", END).strip(),
               address_line1txt.get("1.0", END).strip(), address_line2txt.get("1.0", END).strip(),
               baranggaytxt.get("1.0", END).strip(), municipalittxt.get("1.0", END).strip(),
               provincetxt.get("1.0", END).strip(), zip_codetxt.get("1.0", END).strip(),
               countrytxt.get("1.0", END).strip(), picturepathtxt.get("1.0", END).strip(),
               employee_numbertxt.get("1.0", END).strip()))
    conn.commit()
    conn.close()

window = tk.Tk()
window.title("Employee Information Form")
window.geometry('1500x900')

class employee_info_form():
    def frames(self, x, y):
        self.frame1 = Frame(window, width=1100, height=160, border=0, bg='#CDD6DB')
        self.frame1.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=20, height=1, fg='dark blue', bg='white', font=('Verdana', 11, 'bold'))
        self.textbox.place(x=x, y=y)
        return self.textbox

    def textbox_design2(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='white', font=('Verdana', 11, 'bold'))
        self.textbox.place(x=x, y=y)
        return self.textbox

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='dark blue', bg='#CDD6DB', font=('Arial', 10, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='dark blue', font=('Arial', 30, 'bold'))
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y, text, command):
        self.button = Button(width=15, pady=7, text=text, bg='#3E64dA', fg='white', cursor='hand2',
                                    border=0, command=command)
        self.button.place(x=x, y=y)


emp_design = employee_info_form()
emp_design.frames(200, 220)
emp_design.frames(200, 390)
emp_design.frames(200, 560)

biglbl = emp_design.label_design2(520, 100, 'EMPLOYEE INFORMATION')

image_path = "icon.png"
img = Image.open(image_path)
img = ImageTk.PhotoImage(img)

# Create a label to display the image
image_label = Label(window, image=img)
image_label.image = img  # To keep a reference
image_label.place(x=215, y=150)

firstnametxt = emp_design.textbox_design1(440, 262)
middle_nametxt = emp_design.textbox_design1(x=649, y=262)
surnametxt = emp_design.textbox_design1(x=858, y=262)
suffixtxt = emp_design.textbox_design1(1067, 262)
date_of_birthtxt = emp_design.textbox_design1(440, 330)
nationalitytxt = emp_design.textbox_design1(1067, 330)

departmenttxt = emp_design.textbox_design2(232, 500)
designationtxt = emp_design.textbox_design2(495, 500)
employee_statustxt = emp_design.textbox_design2(760, 500)
employee_numbertxt = emp_design.textbox_design2(1025, 500)
contact_numbertxt = emp_design.textbox_design2(232, 435)
email_addresstxt = emp_design.textbox_design2(495, 435)
other_social_mediatxt = emp_design.textbox_design2(760, 435)
social_media_accounttxt = emp_design.textbox_design2(1025, 435)

address_line1txt = emp_design.textbox_design2(232, 600)
address_line2txt = emp_design.textbox_design2(495, 600)
baranggaytxt = emp_design.textbox_design2(760, 600)
municipalittxt = emp_design.textbox_design2(1025, 600)
provincetxt = emp_design.textbox_design2(232, 670)
zip_codetxt = emp_design.textbox_design2(498, 670)
countrytxt = emp_design.textbox_design2(764, 670)
picturepathtxt = emp_design.textbox_design2(1025, 670)

firstname_lbl = emp_design.label_design(440, 235, 'Firstname')
middle_namelbl = emp_design.label_design(650, 235, 'Middlename')
surnamelbl = emp_design.label_design(858, 235, 'Surname')
suffixlbl = emp_design.label_design(1067, 235, 'Suffix')
date_of_birthlbl = emp_design.label_design(440, 305, 'Date of Birth')
nationalitylbl = emp_design.label_design(1067, 305, 'Nationality')
civil_statuslbl = emp_design.label_design(858, 305, 'Civil Status')
genderlbl = emp_design.label_design(650, 305, 'Gender')

departmentlbl = emp_design.label_design(232, 410, 'Department')
designationlbl = emp_design.label_design(498, 410, 'Designation')
emp_statuslbl = emp_design.label_design(764, 410, 'Employee Status')
emp_numberlbl = emp_design.label_design(1030, 410, 'Employee Number')
emp_contact_numlbl = emp_design.label_design(232, 475, 'Contact Number')
emp_email_addlbl = emp_design.label_design(498, 475, 'Email Address')
emp_other_social_media_accountlbl = emp_design.label_design(764, 475, 'Other Social Media Account')
emp_social_media_accountlb = emp_design.label_design(1030, 475, 'Social Media Account')

address_line1_lbl = emp_design.label_design(232, 575, 'Address 1 ')
address_line2_lbl = emp_design.label_design(495, 575, 'Address 2 (Optional)')
baranggay_lbl = emp_design.label_design(760, 575, 'Baranggay')
municipalit_lbl = emp_design.label_design(1025, 575, 'Municipality')
province_lbl = emp_design.label_design(232, 645, 'Province')
zip_code_lbl = emp_design.label_design(498, 645, 'Zip Code')
country_lbl = emp_design.label_design(764, 645, 'Country')

gender_var = tk.StringVar()
gender_var.set(' Select ')
combo_field = ttk.Combobox(window, width=20, textvariable=gender_var)
combo_field['values'] = (' Select ', ' Female', ' Male ', ' Prefer not to Say')
combo_field.place(x=650, y=330)

civil_status_var = tk.StringVar()
civil_status_var.set(' Single')
combo_field1 = ttk.Combobox(window, width=20, textvariable=civil_status_var)
combo_field1['values'] = (' Single', ' Married ', ' Widow', ' Legally Separated', ' Annulled')
combo_field1.place(x=858, y=330)

emp_design.button_design(440, 750, 'Save', save_data)
emp_design.button_design(600, 750, 'Search', search_data)
emp_design.button_design(760, 750, 'Update', update_data)
emp_design.button_design(920, 750, 'Clear', clear_fields)

init_db()

window.mainloop()