'''

# Task 1: Dictionary Creation & Access

# Exercise 1: Student Dictionary
# Create a dictionary with: "name": "Ravi", "age": 16, "grade": "B", Print only the "grade".

student_details = {"name":"Ravi", "age":16, "grade": "B"}
print(student_details)
print(student_details["grade"])

# Exercise 2: Car Dictionary
# Create a dictionary with: "brand": "Toyota", "model": "Innova", "year": 2021, Print the "model" and "year".

car_details = {"brand":"Toyota", "model":"Innova", "year":"2021"}
print(car_details)
print(car_details["model"],car_details["year"])

# Exercise 3: Book Dictionary
# Create a dictionary with: "title": "The Alchemist", "author": "Paulo Coelho", "pages": 197, Print the "author".

book_details = {"title": "The Alchemist", "author": "Paulo Coelho", "pages": 197}
print(book_details)
print(book_details["author"])

# Task 2: Add and Update Keys

# Exercise 1: Add & Update – User
# Start with: user = {"name": "Anu"}, Add "age" = 25, Add "city" = "Chennai", Update "name" to "Anusha", Print the dictionary after each step.

user = {"name": "Anu"}
print(user)
user["age"] = 25
user["City"] = "Chennai"
print(user)

user["name"] = "Anusha"
print(user)

x = user["name"]
print(x)

y = user.get("name")
print(y)

# Exercise 2 – Laptop Dictionary Task
# Start with: laptop = {"brand": "HP"} Then: Add "RAM" = "16GB", Add "SSD" = "512GB", Update "brand" to "Dell"

laptop_details = {"brand": "HP"}
print(laptop_details)
laptop_details["RAM"] = "16GB"
print(laptop_details)
laptop_details["SSD"] = "512GB"
print(laptop_details)
laptop_details["brand"] = "Dell"
print(laptop_details)

# Exercise 3 – Movie Dictionary Task
# Start with: movie = {"title": "Interstellar"} Then: Add "year" = 2014, Add "genre" = "Sci-Fi", Update "title" to "Inception"

movie_details = {"title": "Interstellar"}
print(movie_details)
movie_details["year"] = "2014"
print(movie_details)
movie_details["genre"] = "Sci-Fi"
print(movie_details)
movie_details["title"] = "Inception"
print(movie_details)

# Task 3: Delete Keys

# Exercise 1: User Dictionary
# Start with: user = {"name": "Anu", "age": 25, "city": "Chennai"} Then: Remove "city" using .pop(), Remove "age" using del


######

# Q1 – Easy: Access Nested Value
# You have this dictionary:

student = {
    "name": "Ravi",
    "details": {
        "age": 16,
        "grade": "A"
    }
}

# Task: Print "grade" value from the dictionary.




myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

#print(myfamily)


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

#print(child1)
#print(child2)
#print(child3)
#print(myfamily)


#print(myfamily["child1"]["name"])
#print(myfamily["child2"],["year"])


for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])




my_family = {

"child1" : {"name":"sid","age":"22"} 



}

#print(my_family)
#print(my_family["child1"]["age"])


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["model"])
x = thisdict["model"]
print(x)

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

print(car)



x = car.items()

print(x) #before the change

car["color"] = "red"

#print(x) #after the change 
print(car)



mydict = {"name":"siddhu", "age":30, "city":"coimbatore"}
print("Before clear: ",mydict)

mydict.clear()
print("After clear: ",mydict)

thisdict = {"name":"suresh","age":40,"city":"bangalore"}
print("Before :", thisdict)

thisdict.clear()
print("After: ", thisdict)

thisdict["status"] = "active"
print("New key: ", thisdict)

thisdict = {"name":"suresh","age":40,"city":"bangalore"}
print("Before: ", thisdict)

thisdict.clear()
print("After: ", thisdict)

print(len(thisdict))

myfamily = {
    "child1": {
        "name": "Amit",
        "age": 10
    },
    "child2": {
        "name": "Rita",
        "age": 8
    }
}

print("Before: ", myfamily)

myfamily["child1"].clear()  
print("after: ", myfamily)

dict1 = {"name": "siddhu", "age": 25}
print(dict1)
dict2 = dict1.copy()
print(dict2)

dict1.clear()
print("dict1:", dict1)
print("dict2:", dict2)


user_details = {"name":"sheffi", "age" : 25}
print(user_details)
user_details_1 = user_details.copy()
print(user_details_1)

user_details.clear()
print(user_details)
print(user_details_1)

bike_details = {"company":"bajaj", "model":"pulsar", "year":2020}
print(bike_details)
bike_details_1 = bike_details.copy()
print(bike_details_1)
bike_details["year"] = 2024
print(bike_details)
print(bike_details_1)

car_details = {"company":"skoda", "model":"rapid", "year":2024}
print(car_details)
car_details_1 = car_details.copy()
print(car_details_1)
car_details_1["date"]="12.01.2024" 
print(car_details_1)
print(car_details)
car_details_1["model"] = "Octavia"
print(car_details_1)


original = {
    "student": {
        "name": "Anu",
        "age": 19
    }
}

# Task 1 (Simple)
user = {"name": "Amit", "age": 22}
print(user.get("name"))  # Try to get the name

copied = original.copy()

# Change name in copied dictionary
copied["student"]["name"] = "Ravi"

print("Original:", original)
print("Copied:", copied)


user = {"name": "Amit", "age": 22}
print(user)
print(user.get("name"))

user = {"name": "Amit", "age": 22}
print(user)
print(user.get("city"))



for item in range[10, 20, 30]:
    print(item)

    for i in range(5):
      print(i)
'''

# Q1. Create a dictionary of a student with keys "name", "age", and "grade". Print the dictionary.


def student_details():
  student = {"name" : "sid", "age" : 30, "grade": "a" }
  print(student)
  print(student["grade"])
  student["city"] = "mumbai"
  print(student)
 
student_details()


user = {"name": "Ravi", "age": 25}

print(user.get("age"))
print(user.get("city"))




















