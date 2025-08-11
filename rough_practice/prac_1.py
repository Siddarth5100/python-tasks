'''

fruits = ["apple","banana","Kiwi"]
print(fruits[-1])
fruits.append("grape")
fruits.remove("banana")
fruits.sort()
for i in fruits:
    if "apple" in i:
        print(i)
print(fruits)


my_list = [10,20,30,"apple"]
print(my_list)

my_list.append("banana")
print(my_list)

my_list.insert(1,"grape")
print(my_list)


for i in range(1,6):
    print(i)
        
for char in ("hello"):
    print(char)

for i in range(1,11):
    if i % 2 == 0:
        print(i, end=" ")



this_list = list(("apple","mango","Kiwi"))
print(len(this_list))

list_1 = ["apple","banana","cherry"]
list_2 = [1,2,3,4,5]
list_3 = [True, False, False]

print(list_1)
print(list_2)
print(list_3)

list_4 = ["male","34",True,20.5]
print(list_1)
print(type(list_1))
print(list_1[1])
print(list_4[-2])
print(list_1[1:2])

data = ["1","2","3","4","5","6"]
print(data[-3:-1])
if "1" in data:
    print("Yes")
    data[-2] = 10
    print(data)

i = 1
while i < 6:
  print(i)
  i += 1



emp_list = {"name": "sidhu", "age": 30}
print(emp_list)
emp_list["age"] = 35
print(emp_list)
emp_list["role"] = "software developer"
print(emp_list)

'''

student_details = {"name":"siddarth", "age":30, "grade":"A"}
print(student_details)
print(student_details["grade"])

user = {"username": "sid123", "password": "pass123"}
print("email" in user)

person = {"name": "Anu", "age": 25}
person["City"] = "Mumbai"
print(person)
person["age"]=30
print(person)

user = {"username": "sid123", "password": "pass123"}
print(user)
user.pop("password")
print(user)

car = {"brand": "Honda", "model": "Amaze", "year": 2022}

for i in car:
    print(i)
for x in car:
    print(car[x])

students = {
    "Ravi": {"age": 15, "grade": "A"},
    "Sneha": {"age": 14, "grade": "B"}
}

print(students["Ravi"]["age"])

students = {
    "Ravi": {"age": 15, "grade": "A"},
    "Sneha": {"age": 14, "grade": "B"},
    "Arjun": {"age": 13, "grade": "A"}
}

count = 0
for student in students:
    if students[student]["grade"] == "A":
        count += 1
print(count)





            


































