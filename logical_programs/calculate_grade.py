student_mark = int(input("Enter the marks: "))
if student_mark > 100:
    print("Enter the mark less than 100")
elif student_mark >= 90:
    print("Grade A")
elif student_mark >= 80:
    print("Grade B")
elif student_mark >= 70:
    print("Grade C")
elif student_mark >= 60:
    print("Grade D")
else:
    print("Fail")