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

'''
def palindrome(a):
    num_1 = str(a)
    num_2 = num_1[::-1]
    print(num_2)
    if num_1 == num_2:
        print("correct")
    else:
        print("Wrong")

palindrome(1011)
