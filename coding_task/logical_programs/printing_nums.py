
# Ques : Write a Python program using a for loop to print numbers from 1 to 10 in a single line, with a space between each number.

def num(a,b):
    for n in range(a,b):
        print(n, end=" ")

num(1,11)

#or

def print_numbers():
    for i in range(1, 10):
        print(i, end=" ")

print_numbers()