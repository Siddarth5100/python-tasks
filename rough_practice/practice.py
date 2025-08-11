'''
a,b,c = "apple","orange","berry"
print(a)
print(b)
print(c)

x=y=z = "orange"
print(x)
print(y)
print(z)

fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

x = "awesome"
print(type(x))

def myfun():
    print("python is "+ x )
myfun()

x = 1
a = float(x)
print(a)

count = 1
while count >= 5:
    print(count)
    count += 1


for i in range(1,10):
    print(i , "* 3 =", i * 3)

a = int(input("Enter the num A = " ))
b = int(input("Enter the num B = "))

for i in range(a+1,b):
    print(i)


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

Write a function that takes a number and prints whether it's even or odd.
✅ Topics: if, % operator, function


def even_odd(num):
    if num % 2 == 0:
        print("This is even number!")
    else:
        print("It is odd number")

even_odd(21)

2. Sum from 1 to N

Take input n and use a loop to find the sum of numbers from 1 to n.
✅ Topics: for loop, range, operators

def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    print("Sum of digits =", total)

sum_of_digits(123)


Write a Python function that takes a number and prints its factorial.

🧮 Example:

    Input: 5

    Output: Factorial of 5 is 120
    (Because 5 × 4 × 3 × 2 × 1 = 120)

    

def factorial_number(number):
    print("Number entered")
    result = 1



factorial_number(5)


Q3: Check if a number is a palindrome

A palindrome number is a number that reads the same forward and backward.
Example: 121, 1331, 12321 are palindrome numbers.


def palindrome(a):
    num_1 = str(a)
    num_2 = num_1[::-1]
    print(num_2)
    if num_1 == num_2:
        print("correct")
    else:
        print("Wrong")

palindrome(1011)


x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

x = 5
y = "john"

print(type(x))
print(type(y))

x,y,z = "apple", "banana", "cherry"
print(x)
print(y)
print(z)


def sep_values():

    values = [1,2,"banana", 3.2 , "Siddhu"]
    a = []
    b = []
    c = []  
    for i in values:
        if type(i) == int:
            a.append(i)
        if type(i) == str:
            b.append(i)
        if type(i) == float:
            c.append(i)

    print(a) 
    print(b)
    print(c)

     


sep_values()


def separate_value():
    a = []  # to store integers
    b = []  # to store strings
    c = []  # to store floats
    values = [1, 2, "apple", 3.10, "kiwi"]

    for item in values:
        if type(item) == int:
            a.append(item)
        elif type(item) == str:
            b.append(item)
        elif type(item) == float:
            c.append(item)

    print("Integers:", a)
    print("Strings:", b)
    print("Floats:", c)

separate_value()


for i in "apple":
    print(i)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 


print(bool('Hello'))
print(bool("15"))

def my_function():
    return False

print(my_function())

x = 5
x += 3
print(x)


print(10>9)
print(10==9)
print(10<9)

a = 100
b = 190

if a > b:
    print("A is greater!")
else:
    print("B is greater")


print(bool("siddhu"))
print(bool(90))
print(bool(" "))
print(bool(0))
print(bool("10"))
print(bool())
print(bool(""))

x = "siddhu"
y = 20
z = ""

print(bool(x))
print(bool(y))
print(bool(z))

print(bool(None))

def my_function():
    return False

if my_function():
    print("Yes!")
else:
    print("No")

x = "100"
print(isinstance(x,int))


print(10+5)

print(5 + 4 - 7 + 3) 

x = 10
y = 20

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

x =10
y =15

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)


x=19
print(not(x<5 and x<10))

print(x:=3)

thislist = ["siddhu", "Vijay", " arun"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print(type(thislist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

a = list("siddhu")
print(a)



user_input = input("Enter a word: ")
char_list = list(user_input)
print("List of chracters: ", char_list)


digits = input("Enter numbers: ")
digits_list = list(digits)
print(digits_list)


numbers = input("Enter numbers with space: ")
numbers_digit = numbers.split()
print(numbers_digit) 



this_list = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(this_list[-4:-2])

thislist = ["applee", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 
else:
  print("No, it is not there")
'''
num = 12

while num < 10:
    print(num)
