
# Ques : Write a program to take a name as input and print:
# Length of the name. The name in uppercase. The name in reverse. Use string functions like len(), .upper(), and slicing.

def my_functions():
    name = input("Enter the name = ")
    length = len(name)
    u = name.upper()
    r = name[::-1]
    print("The length of the name is : " ,length)
    print("Uppercase: ", u)
    print("Reverse: ", r)

my_functions()
