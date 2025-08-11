'''
# Create a list of fruits: ["apple", "banana", "cherry"].
#Add "mango" to the end of the list. Replace "banana" with "grape". Print the final list.

fruits = ["apple", "banana", "cherry"] 
fruits.append("mango")
print(fruits)

fruits[1] = "grapes"
print(fruits)


numbers = [3, 7, 2, 8, 5, 10]

for i in numbers:
    if i % 2 == 0:
        print("The number is even:", i)

        
name  = "Siddarth" 
age = 30
skills = ["python"," sql","frappe"]

print("My name is",name,",my age is",age,",my skills to upgrade",skills[0],skills[1],skills[2])



car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car)

x =car.keys()
print(x)

car["color"] = "black"

print(x)

if "year" in car:
    print("yes")
else:
    print("No") 


student = {
    "name":"siddarth",
    "age":30,
    "skills": ["python", "sql", "frappe"]    
}

print(student)

print(student["name"])
student["city"] = "Bangalore"
print(student)
student["age"] = 28
print(student)


students = [{"name":"sid","age": 30, "city" : "coimbatore"},
            {"name":"kamal","age":31,"city": "chennai"},
            {"name":"rajin","age":32,"city":"bangalore"}]

print(students)

print(students[1]["name"])
students[2]["city"]= "Chennai"
print(students)


def student_info(name,age,city):
    print("Name", name , "age", age, "city" , city)

student_info("sid",30,"cbe")
student_info("rajini",31,"bangalore")
student_info("kamal",31,"chnnai")

'''


