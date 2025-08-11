'''

this_dict = {"brand":"ford","electric":False, "model":"mutang", "year":"1964","year":"1995", "colors": ["red","white","black"]}
print(this_dict)
print(this_dict["brand"])
print(len(this_dict))
print(type(this_dict))

this_dict1 = dict(name = "Sid", age = 30, country = "Norway")
print(this_dict1)

x = this_dict1.keys()
print(x)



# Q1. Basic Dictionary Creation and Access

# Task : Create a dictionary with 3 key-value pairs: "name" as your name, "city" as your city, "age" as any number

# Then : Print the whole dictionary. Print only the value of "city". Print the value of "age" using .get()

def creation_access():
    this_list = {"Name":"siddhu","City":"coimbatore","Age": 30}
    print(this_list)
    print(this_list["City"])

    age = this_list.get("Age")
    print(age)

creation_access()


# Q2. Update and Add Key-Value Pairs

# Task : Start with this dictionary:

#student = {
#   "name": "Siddhu",
#   "course": "Python",
#   "duration": "3 weeks"
#   }
# Then do the following: Change the "duration" to "4 weeks". Add a new key "completed" with value False. Print the final dictionary.

student = {"name":"siddhu","course":"python","duration":"3 weeks"}

def update_add():
    print(student)

    student["duration"] = "4weeks"
    print(student)

    student["completed"] = False
    print(student)

    print("The final dictionary is :", student)
    
update_add()



# Q3. Access Dictionary Values Safely

# Task : Given the dictionary:

# person = {
#    "name": "Ravi",
#    "city": "Chennai",
#    "age": 28
#     }

# Do the following: Print the value of "city" using direct access. Try to print the value of "email" using .get(). 
# If "email" is not found, it should print "Not provided"

person = {"name":"Ravi","city":"chennai","age":28}
print(person)

print(person["city"])

e_mail = person.get("E-mail", "Not provided")
print(e_mail)

'''

# Q: You have a dictionary of students with their marks. Find the student(s) with the highest marks.
# students = {"Anu": 85,"Ravi": 92,"Meena": 78,"John": 92,"Kiran": 89}

students = {"Anu": 85,"Ravi": 92,"Meena": 78,"John": 92,"Kiran": 89}
print("Details of students & marks: ", students)

top_marks = []

def higest_mark():
    max_marks = max(students.values())
    for name, marks in students.items():
        if marks == max_marks:
            top_marks.append(name)

print("The top marks is: ", top_marks)
 







