students = {
    "S1001": {
        "name" : "kamal",
        "batch" : "2024",
        "attendance" : {
            "total_days" : 200,
            "present_days" : 150
        },
        "terms" : {
            "term_1" : {
                "maths" : 90,
                "english" : 80,
                "tamil" : 70
            },
            "term_2" : {
                "maths" : 95,
                "english" : 85,
                "tamil" : 75
            }
        }
    },

    "S1002" : {
        "name" : "shruthi",
        "batch" : "2024",
        "attendance" : {
            "total_days" : 200,
            "present_days" : 160
        },
        "terms" : {
            "term_1" : {
                "maths" : 95,
                "english" : 85, 
                "tamil" : 75
            },
            "term_2" : {
                "maths" : 96,
                "english" : 86,
                "tamil" : 76
            }
        }

    },

    "S1003" : {
        "name" : "rajini",
        "batch" : "2024",
        "attendance" : {
            "total_days" : 200,
            "present_days" : 170
        },
        "terms" : {
            "term_1" : {
                "maths" : 80,
                "english" : 90,
                "tamil" : 100
            },
            "term_2" : {
                "maths" : 97,
                "english" : 87,
                "tamil" : 95
            }
        }
    }
}

# Q4: Subject-wise Term Marks Summary, Task: For each student, print their name and marks in each subject for Term 1 and Term 2.
'''Student: Suresh
Term 1:
  Maths: 88
  Physics: 92
  English: 81
Term 2:
  Maths: 91
  Physics: 94
  English: 89'''

print (students)
print()
print()
print("*" * 50)

for student_details in students:
    print("student id :", student_details,"    student :", students[student_details]["name"])
    print()
    print()

    terms = students[student_details]["terms"]
    print(terms)
    for term_name in terms:
        print(term_name + ":")
        subjects = terms[term_name]
       #print(subjects)
        for subject in subjects:
            print(" ", subject + ":", subjects[subject])

    print()
    print("^" * 35)







'''

# S1001 - Present: 210 / Total: 260 , Q2: Print each student's total and present attendance like this:
# For each student, calculate their attendance percentage , S1001 - Attendance: 80.77%

for student_id in students:
    print(student_id)
    attendance = students[student_id]["attendance"]
    print("To calculate: ", attendance)
    
    present_days = students[student_id]["attendance"]["present_days"]
    print("present_days", present_days)
    total_days = students[student_id]["attendance"]["total_days"]
    print("total_days", total_days)

    percentage = (present_days /total_days) * 100
 
    print("student id :", student_id, "attendance :",total_days, "Attendance % :", percentage )

for student_id in students:
    print(student_id)
    attendance = students[student_id]["attendance"]
    print("To calculate: ", attendance)
    
    present_days = attendance["present_days"]
    print("present_days:", present_days)

    total_days = attendance["total_days"]
    print("total_days:", total_days)

    percentage = (present_days / total_days) * 100

    print("Student ID:", student_id)
    print("Attendance: {}/{} ({:.2f}%)".format(present_days, total_days, percentage))
    print("-" * 40)
    print("-" * 45)




for student_id in students:
    attendance = students[student_id]["attendance"]
    
    present = attendance["present_days"]
    total = attendance["total_days"]
    
    percentage = (present / total) * 100
    
    print("student id:", student_id, "attendance:", round(percentage, 2), "%")


for student_id in students: 
    pres = students[student_id]["attendance"]["present_days"]
    total = students[student_id]["attendance"]["total_days"]
    print(student_id ,"- Present: " ,pres ,"/ Total: ", total)


detail = {"name": "sid"}
print(detail)
for x in detail:
    print(detail[x])

detail = {}



for x in students:
    print(students[x]["name"])

# student id: S1003 name: rahul  

for id in students:
    print("student id :", id,"name :" , students[id])
'''
