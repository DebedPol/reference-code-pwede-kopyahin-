import tkinter as tk
from tkinter import messagebox
import sqlite3

class SeriPayroll:
    def __init__(self, frame):
        self.frame = frame

    def create_label(self, text, x, y, font_weight="normal"):
        label = tk.Label(self.frame, text=text, font=('Arial', 10, font_weight), fg='dark blue', bg='#CDD6DB')
        label.place(x=x, y=y)
        return label

    def create_entry(self, x, y):
        entry = tk.Entry(self.frame, width=30)
        entry.place(x=x, y=y)
        return entry

    def create_button(self, text, x, y, bg_color, fg_color, width):
        button = tk.Button(self.frame, text=text, bg=bg_color, fg=fg_color, width=width)
        button.place(x=x, y=y)
        return button

class Employee:
    def __init__(self, emp_data):
        self.company_name = emp_data.get("company_name")
        self.employee_department = emp_data.get("employee_department")
        self.employee_name = emp_data.get("employee_name")
        self.employee_code = emp_data.get("employee_code")
        self.salary_cut_off = emp_data.get("salary_cut_off")
        self.emp_rate_per_hour = float(emp_data.get("emp_rate_per_hour"))
        self.emp_num_of_hours_per_payday = int(emp_data.get("emp_num_of_hours_per_payday"))
        self.emp_hour_overtime = float(emp_data.get("emp_hour_overtime"))
        self.honorarium_pay = float(emp_data.get("honorarium_pay"))
        self.emp_num_of_absences = int(emp_data.get("emp_num_of_absences"))
        self.emp_num_tardiness = int(emp_data.get("emp_num_tardiness"))

        self.calculate_basic_pay()
        self.calculate_overtime_pay()
        self.calculate_gross_earnings()
        self.calculate_philhealth_contribution()
        self.calculate_sss_contribution()
        self.calculate_tardiness_deduction()
        self.calculate_absences_deduction()
        self.calculate_total_deduction()
        self.calculate_net_income()

    def calculate_basic_pay(self):
        self.basic_pay = self.emp_rate_per_hour * self.emp_num_of_hours_per_payday

    def calculate_overtime_pay(self):
        self.overtime_pay = self.emp_rate_per_hour * 1.25 * self.emp_hour_overtime

    def calculate_gross_earnings(self):
        self.emp_gross_earnings = self.basic_pay + self.overtime_pay + self.honorarium_pay

    def calculate_philhealth_contribution(self):
        self.philhealth_contribution = 200.00  # Placeholder for actual calculation

    def calculate_sss_contribution(self):
        sss_table = [
            (4250, 180.00), (4750, 202.50), (5250, 217.50), (5749.99, 260.24),
            (6249.99, 270.00), (6749.99, 292.50), (7249.99, 315.00), (7749.99, 337.50),
            (8249.99, 360.00), (8749.99, 382.50), (9249.99, 405.00), (9749.99, 427.50),
            (10249.99, 450.00), (10749.99, 472.50), (11249.99, 495.00), (11749.99, 517.50),
            (12249.99, 540.00), (12749.99, 562.50), (13249.99, 585.00), (13749.99, 607.50),
            (14249.99, 630.00), (14749.99, 652.50), (15249.99, 675.00), (15749.99, 697.50),
            (16249.99, 720.00), (16749.99, 742.50), (17249.99, 765.00), (17749.99, 787.50),
            (18249.99, 810.00), (18749.99, 832.50), (19249.99, 855.00), (19749.99, 877.50),
            (20249.99, 900.00), (float('inf'), 900.00)
        ]

        for limit, contribution in sss_table:
            if self.emp_gross_earnings <= limit:
                self.sss_contribution = contribution
                break

    def calculate_tardiness_deduction(self):
        tardiness_per_hour = self.emp_rate_per_hour / 60
        self.tardiness_deduction = tardiness_per_hour * self.emp_num_tardiness

    def calculate_absences_deduction(self):
        absences_per_hour = self.emp_rate_per_hour * 8  # Assuming an 8-hour workday
        self.absences_deduction = absences_per_hour * self.emp_num_of_absences

    def calculate_total_deduction(self):
        self.total_deduction = (
            self.philhealth_contribution +
            self.sss_contribution +
            self.tardiness_deduction +
            self.absences_deduction
        )

    def calculate_net_income(self):
        self.net_income = self.emp_gross_earnings - self.total_deduction

def compute_income_and_deductions():
    try:
        emp_data = {
            "company_name": company_name_entry.get(),
            "employee_department": employee_department_entry.get(),
            "employee_name": employee_name_entry.get(),
            "employee_code": employee_code_entry.get(),
            "salary_cut_off": salary_cut_off_entry.get(),
            "emp_rate_per_hour": emp_rate_per_hour_entry.get(),
            "emp_num_of_hours_per_payday": emp_num_of_hours_per_payday_entry.get(),
            "emp_hour_overtime": emp_hour_overtime_entry.get(),
            "honorarium_pay": honorarium_pay_entry.get(),
            "emp_num_of_absences": emp_num_of_absences_entry.get(),
            "emp_num_tardiness": emp_num_tardiness_entry.get()
        }

        employee = Employee(emp_data)

        honorarium_income_entry.delete(0, tk.END)
        honorarium_income_entry.insert(0, f"{employee.honorarium_pay:.2f}")

        sss_contribution_entry.delete(0, tk.END)
        sss_contribution_entry.insert(0, f"{employee.sss_contribution:.2f}")

        philhealth_contribution_entry.delete(0, tk.END)
        philhealth_contribution_entry.insert(0, f"{employee.philhealth_contribution:.2f}")

        total_deduction_entry.delete(0, tk.END)
        total_deduction_entry.insert(0, f"{employee.total_deduction:.2f}")

        gross_income_entry.delete(0, tk.END)
        gross_income_entry.insert(0, f"{employee.net_income:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Database functions
def create_db():
    con = sqlite3.connect("Payroll_Finals.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS personal_infotbl (
        company_name TEXT,
        employee_department TEXT,
        employee_name TEXT,
        employee_code TEXT PRIMARY KEY,
        salary_cut_off TEXT,
        emp_rate_per_hour REAL,
        emp_num_of_hours_per_payday INTEGER,
        emp_hour_overtime REAL,
        honorarium_pay REAL,
        emp_num_of_absences INTEGER,
        emp_num_tardiness INTEGER
    )''')
    con.commit()
    con.close()

def insert_employee(emp_data):
    con = sqlite3.connect("Payroll_Finals.db")
    cur = con.cursor()
    cur.execute('''INSERT INTO personal_infotbl (
        company_name, employee_department, employee_name, employee_code, salary_cut_off,
        emp_rate_per_hour, emp_num_of_hours_per_payday, emp_hour_overtime, honorarium_pay,
        emp_num_of_absences, emp_num_tardiness
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
        emp_data["company_name"], emp_data["employee_department"], emp_data["employee_name"],
        emp_data["employee_code"], emp_data["salary_cut_off"], emp_data["emp_rate_per_hour"],
        emp_data["emp_num_of_hours_per_payday"], emp_data["emp_hour_overtime"], emp_data["honorarium_pay"],
        emp_data["emp_num_of_absences"], emp_data["emp_num_tardiness"]
    ))
    con.commit()
    con.close()

def update_employee(emp_data):
    con = sqlite3.connect("Payroll_Finals.db")
    cur = con.cursor()
    cur.execute('''UPDATE personal_infotbl SET
        company_name = ?, employee_department = ?, employee_name = ?, salary_cut_off = ?,
        emp_rate_per_hour = ?, emp_num_of_hours_per_payday = ?, emp_hour_overtime = ?, honorarium_pay = ?,
        emp_num_of_absences = ?, emp_num_tardiness = ?
        WHERE employee_code = ?''', (
        emp_data["company_name"], emp_data["employee_department"], emp_data["employee_name"],
        emp_data["salary_cut_off"], emp_data["emp_rate_per_hour"], emp_data["emp_num_of_hours_per_payday"],
        emp_data["emp_hour_overtime"], emp_data["honorarium_pay"], emp_data["emp_num_of_absences"],
        emp_data["emp_num_tardiness"], emp_data["employee_code"]
    ))
    con.commit()
    con.close()

def search_employee(employee_code):
    con = sqlite3.connect("Payroll_Finals.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM personal_infotbl WHERE employee_code = ?", (employee_code,))
    emp_data = cur.fetchone()
    con.close()
    if emp_data:
        return {
            "company_name": emp_data[0],
            "employee_department": emp_data[1],
            "employee_name": emp_data[2],
            "employee_code": emp_data[3],
            "salary_cut_off": emp_data[4],
            "emp_rate_per_hour": emp_data[5],
            "emp_num_of_hours_per_payday": emp_data[6],
            "emp_hour_overtime": emp_data[7],
            "honorarium_pay": emp_data[8],
            "emp_num_of_absences": emp_data[9],
            "emp_num_tardiness": emp_data[10]
        }
    return None

# GUI Functions
def show_message(message):
    messagebox.showinfo("Info", message)

def save_employee():
    emp_data = {
        "company_name": company_name_entry.get(),
        "employee_department": employee_department_entry.get(),
        "employee_name": employee_name_entry.get(),
        "employee_code": employee_code_entry.get(),
        "salary_cut_off": salary_cut_off_entry.get(),
        "emp_rate_per_hour": float(emp_rate_per_hour_entry.get()),
        "emp_num_of_hours_per_payday": int(emp_num_of_hours_per_payday_entry.get()),
        "emp_hour_overtime": float(emp_hour_overtime_entry.get()),
        "honorarium_pay": float(honorarium_pay_entry.get()),
        "emp_num_of_absences": int(emp_num_of_absences_entry.get()),
        "emp_num_tardiness": int(emp_num_tardiness_entry.get())
    }
    insert_employee(emp_data)
    show_message("Employee information saved successfully!")

def update_employee_info():
    emp_data = {
        "company_name": company_name_entry.get(),
        "employee_department": employee_department_entry.get(),
        "employee_name": employee_name_entry.get(),
        "employee_code": employee_code_entry.get(),
        "salary_cut_off": salary_cut_off_entry.get(),
        "emp_rate_per_hour": float(emp_rate_per_hour_entry.get()),
        "emp_num_of_hours_per_payday": int(emp_num_of_hours_per_payday_entry.get()),
        "emp_hour_overtime": float(emp_hour_overtime_entry.get()),
        "honorarium_pay": float(honorarium_pay_entry.get()),
        "emp_num_of_absences": int(emp_num_of_absences_entry.get()),
        "emp_num_tardiness": int(emp_num_tardiness_entry.get())
    }
    update_employee(emp_data)
    show_message("Employee information updated successfully!")


def search_employee_info():
    employee_code = employee_code_entry.get()
    emp_data = search_employee(employee_code)
    if emp_data:
        company_name_entry.delete(0, tk.END)
        company_name_entry.insert(0, emp_data["company_name"])
        employee_department_entry.delete(0, tk.END)
        employee_department_entry.insert(0, emp_data["employee_department"])
        employee_name_entry.delete(0, tk.END)
        employee_name_entry.insert(0, emp_data["employee_name"])
        salary_cut_off_entry.delete(0, tk.END)
        salary_cut_off_entry.insert(0, emp_data["salary_cut_off"])
        emp_rate_per_hour_entry.delete(0, tk.END)
        emp_rate_per_hour_entry.insert(0, emp_data["emp_rate_per_hour"])
        emp_num_of_hours_per_payday_entry.delete(0, tk.END)
        emp_num_of_hours_per_payday_entry.insert(0, emp_data["emp_num_of_hours_per_payday"])
        emp_hour_overtime_entry.delete(0, tk.END)
        emp_hour_overtime_entry.insert(0, emp_data["emp_hour_overtime"])
        honorarium_pay_entry.delete(0, tk.END)
        honorarium_pay_entry.insert(0, emp_data["honorarium_pay"])
        emp_num_of_absences_entry.delete(0, tk.END)
        emp_num_of_absences_entry.insert(0, emp_data["emp_num_of_absences"])
        emp_num_tardiness_entry.delete(0, tk.END)
        emp_num_tardiness_entry.insert(0, emp_data["emp_num_tardiness"])


# Database initialization
create_db()

# GUI initialization
window = tk.Tk()
window.title("Se-ri's Choice Payroll")
frame = tk.Frame(window, width=1500, height=800, bg='#CDD6DB')
frame.place(x=1, y=1)
seri_payroll = SeriPayroll(frame)

# Big Title Label
big_title_label = tk.Label(frame, text="ACCOUNTING DEPARTMENT | ", font=('Arial', 30, 'bold'),fg='dark blue', bg='#CDD6DB')
big_title_label.place(x=400, y=11)
big_title_label = tk.Label(frame, text=" PAYROLL MANAGEMENT ", font=('Arial', 25, 'bold'),fg='dark blue', bg='#CDD6DB')
big_title_label.place(x=560, y=60)
# Basic Info Section
seri_payroll.create_label("BASIC INFO SECTION:", 45, 60, font_weight='bold')
company_name_label = seri_payroll.create_label("Company Name:", 50, 90)
company_name_entry = seri_payroll.create_entry(200, 90)
employee_department_label = seri_payroll.create_label("Employee Department:", 50, 120)
employee_department_entry = seri_payroll.create_entry(200, 120)
employee_name_label = seri_payroll.create_label("Employee Name:", 50, 150)
employee_name_entry = seri_payroll.create_entry(200, 150)
employee_code_label = seri_payroll.create_label("Employee Code:", 50, 180)
employee_code_entry = seri_payroll.create_entry(200, 180)
employee_code_label = seri_payroll.create_label("Employee Code:", 50, 180)
employee_code_entry = seri_payroll.create_entry(200, 180)
salary_cut_off_label = seri_payroll.create_label("Salary Cut Off:", 50, 210)
salary_cut_off_entry = seri_payroll.create_entry(200, 210)
emp_rate_per_hour_label = seri_payroll.create_label("Rate per Hour:", 50, 240)
emp_rate_per_hour_entry = seri_payroll.create_entry(200, 240)
emp_num_of_hours_per_payday_label = seri_payroll.create_label("Number of Hours per Payday:", 50, 270)
emp_num_of_hours_per_payday_entry = seri_payroll.create_entry(200, 270)
emp_hour_overtime_label = seri_payroll.create_label("Hour Overtime:", 50, 300)
emp_hour_overtime_entry = seri_payroll.create_entry(200, 300)
honorarium_pay_label = seri_payroll.create_label("Honorarium Pay:", 50, 330)
honorarium_pay_entry = seri_payroll.create_entry(200, 330)
emp_num_of_absences_label = seri_payroll.create_label("Number of Absences:", 50, 360)
emp_num_of_absences_entry = seri_payroll.create_entry(200, 360)
emp_num_tardiness_label = seri_payroll.create_label("Number of Tardiness:", 50, 390)
emp_num_tardiness_entry = seri_payroll.create_entry(200, 390)

# Buttons for Basic Info Section
search_button = seri_payroll.create_button("Search", 650, 180, '#3E64dA', 'dark blue', 10)
search_button.config(command=search_employee_info)  #search function to button

save_button = seri_payroll.create_button("Save", 650, 210, '#3E64dA', 'dark blue', 10)
save_button.config(command=save_employee)  #save function to button

update_button = seri_payroll.create_button("Update", 650, 240, '#3E64dA', 'dark blue', 10)
update_button.config(command=update_employee_info)  #update function to button

compute_button = seri_payroll.create_button("Compute", 650, 360, '#3E64dA', 'dark blue', 10)
compute_button.config(command=compute_income_and_deductions)
# Other Income Section
seri_payroll.create_label("OTHER INCOME SECTION:", 45, 420, font_weight='bold')
other_rate_per_hour_label = seri_payroll.create_label("Rate per Hour:", 50, 460)
other_rate_per_hour_entry = seri_payroll.create_entry(200, 460)
other_num_of_hours_label = seri_payroll.create_label("Number of Hours:", 50, 490)
other_num_of_hours_entry = seri_payroll.create_entry(200, 490)
honorarium_income_label = seri_payroll.create_label("Honorarium Income:", 50, 520)
honorarium_income_entry = seri_payroll.create_entry(200, 520)
#total_income_label = seri_payroll.create_label("Total Income:", 50, 540)
#total_income_entry = seri_payroll.create_entry(200, 540)

# Other Deduction Section
seri_payroll.create_label("OTHER DEDUCTION SECTION:", 40, 570, font_weight='bold')
sss_contribution_label = seri_payroll.create_label("SSS Contribution:", 50, 600)
sss_contribution_entry = seri_payroll.create_entry(200, 600)
philhealth_contribution_label = seri_payroll.create_label("PhilHealth:", 50, 630)
philhealth_contribution_entry = seri_payroll.create_entry(200, 630)
pagibig_contribution_label = seri_payroll.create_label("PagIbig Contribution:", 50, 660)
pagibig_contribution_entry = seri_payroll.create_entry(200, 660)
pagibig_contribution_entry.insert(0, "100")  # Set the entry to a constant value of 100
pagibig_contribution_entry.config(state='readonly')  # Make the entry read-only
seri_payroll.create_label("TOTAL DEDUCTION", 50, 690, font_weight='bold')
total_deduction_entry = seri_payroll.create_entry(50, 720)

# Gross Income Section
seri_payroll.create_label("GROSS INCOME:", 650, 600, font_weight='bold')
gross_income_label = seri_payroll.create_label("Gross Income:", 680, 630)
gross_income_entry = seri_payroll.create_entry(680, 660)

def save_employee():
    emp_data = {
        "company_name": company_name_entry.get(),
        "employee_department": employee_department_entry.get(),
        "employee_name": employee_name_entry.get(),
        "employee_code": employee_code_entry.get(),
        "salary_cut_off": salary_cut_off_entry.get(),
        "emp_rate_per_hour": float(emp_rate_per_hour_entry.get()),
        "emp_num_of_hours_per_payday": int(emp_num_of_hours_per_payday_entry.get()),
        "emp_hour_overtime": float(emp_hour_overtime_entry.get()),
        "honorarium_pay": float(honorarium_pay_entry.get()),
        "emp_num_of_absences": int(emp_num_of_absences_entry.get()),
        "emp_num_tardiness": int(emp_num_tardiness_entry.get())
    }
    insert_employee(emp_data)
    show_message("Employee information saved successfully!")

def update_employee_info():
    emp_data = {
        "company_name": company_name_entry.get(),
        "employee_department": employee_department_entry.get(),
        "employee_name": employee_name_entry.get(),
        "employee_code": employee_code_entry.get(),
        "salary_cut_off": salary_cut_off_entry.get(),
        "emp_rate_per_hour": float(emp_rate_per_hour_entry.get()),
        "emp_num_of_hours_per_payday": int(emp_num_of_hours_per_payday_entry.get()),
        "emp_hour_overtime": float(emp_hour_overtime_entry.get()),
        "honorarium_pay": float(honorarium_pay_entry.get()),
        "emp_num_of_absences": int(emp_num_of_absences_entry.get()),
        "emp_num_tardiness": int(emp_num_tardiness_entry.get())
    }
    update_employee(emp_data)
    show_message("Employee information updated successfully!")

def search_employee_info():
    employee_code = employee_code_entry.get()
    emp_data = search_employee(employee_code)
    if emp_data:
        company_name_entry.delete(0, tk.END)
        company_name_entry.insert(0, emp_data["company_name"])
        employee_department_entry.delete(0, tk.END)
        employee_department_entry.insert(0, emp_data["employee_department"])
        employee_name_entry.delete(0, tk.END)
        employee_name_entry.insert(0, emp_data["employee_name"])
        salary_cut_off_entry.delete(0, tk.END)
        salary_cut_off_entry.insert(0, emp_data["salary_cut_off"])
        emp_rate_per_hour_entry.delete(0, tk.END)
        emp_rate_per_hour_entry.insert(0, emp_data["emp_rate_per_hour"])
        emp_num_of_hours_per_payday_entry.delete(0, tk.END)
        emp_num_of_hours_per_payday_entry.insert(0, emp_data["emp_num_of_hours_per_payday"])
        emp_hour_overtime_entry.delete(0, tk.END)
        emp_hour_overtime_entry.insert(0, emp_data["emp_hour_overtime"])
        honorarium_pay_entry.delete(0, tk.END)
        honorarium_pay_entry.insert(0, emp_data["honorarium_pay"])
        emp_num_of_absences_entry.delete(0, tk.END)
        emp_num_of_absences_entry.insert(0, emp_data["emp_num_of_absences"])
        emp_num_tardiness_entry.delete(0, tk.END)
        emp_num_tardiness_entry.insert(0, emp_data["emp_num_tardiness"])

# Database functions
def create_db():
    con = sqlite3.connect("Seri_Payroll_Basco.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS personal_infotbl (
        company_name TEXT,
        employee_department TEXT,
        employee_name TEXT,
        employee_code TEXT PRIMARY KEY,
        salary_cut_off TEXT,
        emp_rate_per_hour REAL,
        emp_num_of_hours_per_payday INTEGER,
        emp_hour_overtime REAL,
        honorarium_pay REAL,
        emp_num_of_absences INTEGER,
        emp_num_tardiness INTEGER
    )''')
    con.commit()
    con.close()

def insert_employee(emp_data):
    con = sqlite3.connect("Payroll_Finals.db")
    cur = con.cursor()
    cur.execute('''INSERT INTO personal_infotbl (
        company_name, employee_department, employee_name, employee_code, salary_cut_off,
        emp_rate_per_hour, emp_num_of_hours_per_payday, emp_hour_overtime, honorarium_pay,
        emp_num_of_absences, emp_num_tardiness
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
        emp_data["company_name"], emp_data["employee_department"], emp_data["employee_name"],
        emp_data["employee_code"], emp_data["salary_cut_off"], emp_data["emp_rate_per_hour"],
        emp_data["emp_num_of_hours_per_payday"], emp_data["emp_hour_overtime"], emp_data["honorarium_pay"],
        emp_data["emp_num_of_absences"], emp_data["emp_num_tardiness"]
    ))
    con.commit()
    con.close()

def update_employee(emp_data):
    con = sqlite3.connect("Payroll_Finals.db")
    cur = con.cursor()
    cur.execute('''UPDATE personal_infotbl SET
        company_name = ?, employee_department = ?, employee_name = ?, salary_cut_off = ?,
        emp_rate_per_hour = ?, emp_num_of_hours_per_payday = ?, emp_hour_overtime = ?, honorarium_pay = ?,
        emp_num_of_absences = ?, emp_num_tardiness = ?
        WHERE employee_code = ?''', (
        emp_data["company_name"], emp_data["employee_department"], emp_data["employee_name"],
        emp_data["salary_cut_off"], emp_data["emp_rate_per_hour"], emp_data["emp_num_of_hours_per_payday"],
        emp_data["emp_hour_overtime"], emp_data["honorarium_pay"], emp_data["emp_num_of_absences"],
        emp_data["emp_num_tardiness"], emp_data["employee_code"]
    ))
    con.commit()
    con.close()

def search_employee(employee_code):
    con = sqlite3.connect("Payroll_Finals.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM personal_infotbl WHERE employee_code = ?", (employee_code,))
    emp_data = cur.fetchone()
    con.close()
    if emp_data:
        return {
            "company_name": emp_data[0],
            "employee_department": emp_data[1],
            "employee_name": emp_data[2],
            "employee_code": emp_data[3],
            "salary_cut_off": emp_data[4],
            "emp_rate_per_hour": emp_data[5],
            "emp_num_of_hours_per_payday": emp_data[6],
            "emp_hour_overtime": emp_data[7],
            "honorarium_pay": emp_data[8],
            "emp_num_of_absences": emp_data[9],
            "emp_num_tardiness": emp_data[10]
        }
    return None

window.geometry("1000x800")
window.mainloop()
