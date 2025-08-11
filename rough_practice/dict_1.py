# Step 1: Create a Simple Dictionary

students = {"name":"siddhu","age":30}
print(students)
print(students["name"])
print(students["age"])
print(students.keys())
print(students.values())

students["city"] = "coimbatore"
print(students)
students["name"] = "rakesh"
print(students)

for k in students:
    print(k)

for x,y in students.items():
    print(x,y)

student = {"name": "Karan", "age": 21, "city": "Delhi"}

student["city"] = "Bangalore"
print(student)

student["grade"] = "A" 
print(student)

for student_details in student:
    print(student_details, ":", student[student_details] )


