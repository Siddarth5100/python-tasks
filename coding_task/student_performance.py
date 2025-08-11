import json
import os

print("Current working directory:", os.getcwd())
print()

# A system to manage & analyze student performance (terms, subjects, attendance) 
# Register and manage students(record & update marks per term & subject),(Track attendance),(Generate reports & ranking),(Export/import data using JSON)
# Answer :

students = json.load(open("students.json")) if os.path.exists("students.json") else {}
# Global variable to store the inputs    


# Funtion to register_students:
 
def register_students(student_id,name,batch):   # New student registration
    students[student_id] = {"name": name, "batch": batch}
    
register_students("S1003","Deepan",2025)  # To call function 


# Function to generate_student_report:    

def generate_student_report(student_id):
    if student_id in students:
        name = students[student_id]["name"]
        batch = students[student_id]["batch"]
        print("Student report :", name)
        print("Batch :", batch)
        print()

    else:
        print("Student ID not found")

generate_student_report("S1003")


# Function to record_attendance:

def record_attendance(student_id,total_days,present_days):
    students[student_id]["attendance"] = {"total_days":total_days, "present_days":present_days}

record_attendance("S1003",31,28) # To call function


# Function to add_term_result:

def add_term_result(student_id, term_name, subject_marks_dict):
    if "terms" not in students[student_id]:
        students[student_id]["terms"] = {}    

    students[student_id]["terms"][term_name] = subject_marks_dict 

add_term_result("S1003","Term_1",{"tamil":30,"english":86,"maths":85})   # To call function
     

# Function to update_subject_mark:

def update_subject_mark(student_id, term,subject,new_mark):
    students[student_id]["terms"][term][subject] = new_mark
    
update_subject_mark("S1003","Term_1","english",65)   # To call function


# Function to calculate_average:

def calculate_avg(student_id):
    
    res = {}    # To store result
    for term_name,marks in students[student_id]["terms"].items():
        #print(term_name,marks)
        total_subject_count = 0
        total_marks = 0
        for mark in marks.values():
            #print(mark)
            total_subject_count += 1
            total_marks += mark

        average = total_marks / total_subject_count
        print("Subject average",average)

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
    print("Attendance total :", total_days, "days")
    present_days = students[student_id]["attendance"]["present_days"]
    average = (present_days / total_days) * 100
    return average


print("Attendance percentage :", calculate_attendance_percentage("S1001"))    
print()


calculate_avg("S1003")  # To call function   

# Function to calculate_topper_by_term:  

def get_topper_by_term(term):
    topper_name = ""
    highest_average = 0

    for student_id in students:  # Go to each student
        student = students[student_id]
        name = student["name"]     # Get student data  

        if "terms" in student:       # Check if student has term data
            terms = student["terms"]    # Check if Term_1 exists

            if term in terms:    # Check if this student has the required term   
                subject_marks = terms[term]  # Example: {"Tamil": 90, "English": 95, "Maths": 88}
                
                total = sum(subject_marks.values())
                count = len(subject_marks)
                average = total / count

                if average > highest_average:    # To compare with current highest
                    highest_average = average
                    topper_name = name

    print()
    print("Topper in", term ,"is", topper_name, "with average", highest_average)
    print()

get_topper_by_term("Term_1")

print("Overall pass/fail : ")
print("*" * 19)

def overall_result():
    for student_id in students:
        student = students[student_id]
        name = student["name"]
        
        if "terms" in student:  
            for term, marks in student["terms"].items():
                passed = True

                for mark in marks.values():
                    if mark < 35:
                        passed = False 
                        break

                if passed:
                    print("Student ID:", student_id, "Name:", name, "Term:", term, "Result: Pass")
                else:
                    print("Student ID:", student_id, "Name:", name, "Term:", term, "Result: Fail")

overall_result()


def save_students():
   with open("students.json", "w") as f:
        json.dump(students, f, indent=4)
    
save_students()

print("Data exported to students.json")








