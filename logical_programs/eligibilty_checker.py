# Check if the student is eligible for scholarship based on these conditions: Average marks should be greater than or equal to 80
# Age should be less than 18, Print "Eligible for Scholarship" if both are true, Else, print "Not Eligible"

student = {
    "name": "Arjun",
    "age": 19,
    "marks": {
        "math": 78,
        "science": 85,
        "english": 77
    }
}


#print(student)

marks = student["marks"]
print(marks)
marks_list = marks.values()
print(marks_list)

average = sum(marks_list) / len(marks) 
print(average)

if average >= 80 and student["age"] < 18:
    print("eligible")
else:
    print("not")



    
