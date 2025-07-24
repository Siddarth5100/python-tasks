
'''
name = input("Enter your name here: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
print("My name is : ", name)
print("My age is: ", age)
print("My address is: ", address)


a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))
multiply = (a * b * c)
add = (a + b + c)
divide = (multiply/add)
print("The value is: ", divide)


name = input("Enter name: ")
score = int(input("Enter score for 100: "))
department = input("Enter department: ")
divide = score / 10
print("your score is: ", divide, "/10")



def user_info():
    print("Name: siddhu")
    print("City: Coimbatore")

user_info()


def check_even():
    number_1 = int(input("Enter the number: "))
    if number_1 % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")

check_even()


def find_largest():
    num_1 = int(input("Enter 1st number: "))
    num_2 = int(input("Enter 2nd number: "))
    if num_1 > num_2:
        print("This is greater number: " , num_1)
    elif num_1 == num_2:
        print("Both the numbers are equal")
    elif num_2 > num_1:
        print("This is greater number: ", num_2)
find_largest()

def check_pass_fail():
    num = int(input("Enter the number: "))
    if num > 100:
       print("Invalid input. Marks should be out of 100.")
    elif num >= 40:
         print("You are pass")
    else:
        print("You are fail")


check_pass_fail()

def format_name(name):
    print("Uppercase : " , name.upper())
    print("Lowercase : " , name.lower())
    print("Title: " , name.title())

format_name("siddarth")




Write a function named check_length that takes a string as input and:

    Prints the length of the string.

    Checks if the length is more than 5 characters.

        If yes, print: "Long string"

        If not, print: "Short string"

def check_length(size):
    print("Length of the string is: " , len(size))
    if size > 5:
        print("Long string")
    else:
        print("Short string")

check_length("siddarth")



Write a function called show_name_parts(name) that does the following:

    Prints the first character of the name.

    Prints the last character of the name.

    Prints the first 3 characters.

    Prints the last 3 characters.

def show_name_parts(name):
    print("Answer is : ", name[0])
    print("Answer is : ", name[-1])
    print("Answer is : ", name[0:3])
    print("Answer is : ", name[-3:])
show_name_parts("siddarth")


Write a function check_keyword that takes a string as input.
If the string contains the word "python", print "Python found!".
Else, print "Not found".



def check_keyword(name):
    if "python" in name:
        print("Python found!")
    else:
        print("Python not found")

check_keyword("i love ")

Awesome! Here's your next question:

👉 **Write a function** that checks if the word `"code"` is present in a sentence.

* If found, print `"Code is present!"`
* If not, print `"Code not found."`

You can name the function `check_code_word(sentence)`
Try it!


def word_check(word):
    if "code" in word:
        print("Code is present")
    else:
        print("code not found")

word_check("code is in wordpad")

👉 Write a function to check if a name starts with the letter "S" (case-insensitive).

    If yes, print "Name starts with S"

    Else, print "Name doesn't start with S"

Function name: check_name_start(name)



def check_letter(letter):
    #if letter.startswith("S"):
    if letter.startswith("S"):
        print("Name starts with S")
    else:
        print("Name doesn't start with S")

check_letter("Sddart")

'''

def reverse_letter(word):
    if word == word[:-1]:
        print(word)
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

reverse_letter("alarm")





























