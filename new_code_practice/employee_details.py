
# Task: Create a dictionary employees where:
# Key = employee ID (string like "E1001")
# Value = another dictionary with keys: "name", "department", "salary"

# Write two functions: add_employee(emp_id, name, department, salary) → adds a new employee. 
# update_salary(emp_id, new_salary) → updates salary for the given ID.


employee = {}

def add_employee(emp_id,name,department,salary):
    employee[emp_id] = {"name": name ,"department" : department, "salary" : salary }
    print(employee)
    print(employee[emp_id])
    print("Employee details added successfully!")

add_employee("C1001", "Prakas", "CS", 26500)
add_employee("C1002", "Siddarth", "IT", 26500)
add_employee("C1003", "Riya", "HR", 26500)    
add_employee("C1004", "Priya", "HR", 26500)


def update_salary(emp_id,new_salary):  
    employee[emp_id]["salary"] = new_salary
    print(employee)

update_salary("C1004", 26500)


# Print all employees earning less than ₹28,000.

def less_salary():    
    for emp_id in employee:
        if employee[emp_id]["salary"] < 28000:
            print(emp_id, employee[emp_id]["name"],employee[emp_id]["salary"])

less_salary()


def filter_departmentwise():
    for emp in employee:
       if employee[emp]["department"] == "CS":
            print(emp, employee[emp]["name"])

filter_departmentwise()

print(employee)


def name_starts_letter():
    for name in employee:
        if employee[name]["name"].startswith("P"):
            print("Employee whose name starts with P :", employee[name]["name"], "Department :", employee[name]["department"])

name_starts_letter()

def name_starts_letter():
    letter = input("Enter starting letter: ")
    for emp_id in employee:
        if employee[emp_id]["name"].startswith(letter):
            print("Employee whose name starts with", letter, ":", 
                  employee[emp_id]["name"], 
                  "Department:", employee[emp_id]["department"])

name_starts_letter()

# Task: From the employee dictionary, print all employees who: 
# Are in the "IT" department and have a salary greater than ₹27,000

def department_salary():
    for dept in employee:
        if employee[dept]["department"] == "IT" and employee[dept]["salary"] < 27000:
            print("Employee ID :", dept, "Department :", employee[dept]["department"], "Salary :", employee[dept]["salary"])

department_salary()




