import json


# A system to manage & analyze student performance (terms, subjects, attendance) 
# Register and manage students(record & update marks per term & subject),(Track attendance),(Generate reports & ranking),(Export/import data using JSON)


# Answer :

students = json.loads(open("students.json").read())

print(type(students))

# Function to generate_student_report:    

def generate_student_report(student_id):
    if student_id in students:
        name = students[student_id]["name"]
        batch = students[student_id]["batch"]
        print("Student report :", name)
        print("Batch :", batch)

    else:
        print("Student ID not found")

generate_student_report("S1001")


# Funtion to register_students:
 
def register_students(student_id,name,batch):   # New student registration
    students[student_id] = {"name": name, "batch": batch}
    
register_students("S123","Siddarth",2014)  # To call function 


# Function to record_attendance:

def record_attendance(student_id,total_days,present_days):
    students[student_id]["attendance"] = {"total_days":total_days, "present_days":present_days}

record_attendance("S123",31,28) # To call function


# Function to add_term_result:

def add_term_result(student_id, term_name, subject_marks_dict):
    students[student_id]["terms"] = {term_name : subject_marks_dict }

add_term_result("S123","Term_1",{"tamil":80,"english":85,"maths":83})   # To call function


# Function to update_subject_mark:

def update_subject_mark(student_id, term,subject,new_mark):
    students[student_id]["terms"][term][subject] = new_mark
    
update_subject_mark("S123","Term_1","english",81)   # To call function


# Function to calculate_average:

def calculate_avg(student_id):
    
    res = {}    # To store result
    for term_name,marks in students[student_id]["terms"].items():
        print(term_name,marks)
        total_subject_count = 0
        total_marks = 0
        for mark in marks.values():
            print(mark)
            total_subject_count += 1
            total_marks += mark

        average = total_marks / total_subject_count
        print(average)

        res[term_name] = float(average)
    
    #print(res)

    overall_total = 0
    for term_average in res.values():
        overall_total += term_average

    overall_average = overall_total/ len(res)

    print("Term_wise averages :", res)
    print("Overall average :", overall_average)


# Function to calculate_attendance_percentage:    

def calculate_attendance_percentage(student_id):
    total_days = students[student_id]["attendance"]["total_days"]
    print("Attendance :", total_days)
    present_days = students[student_id]["attendance"]["present_days"]
    average = (present_days / total_days) * 100
    return average

print("Attendance percentage :", calculate_attendance_percentage("S123"))    # To call function 

calculate_avg("S1001")  # To call function




with open("students.json", "w") as f:
    f.write(json.dump(students, f, indent=4))
print("Data exported to students.json")
























#def get_topper_by_term(term):

# print("Total days :", students["S1001"]["attendance"]["total_days"])  # To print the values entered in student

# practice 


# subject = "Tamil"
# mark = 90
# print(students["S1001"]["terms"]["term_2"]["Physics"]) 
# print(students["S1001"]["terms"]["term1"]["physics"])
# students["S1001"]["terms"]["term1"]["physics"] = 50
# students["S1001"]["terms"]["term1"][subject] = mark
# print(students["S1001"]["terms"]["term1"])
# print(students["S1001"]["terms"]["term1"]["physics"])
# print("Details entered: ",students)