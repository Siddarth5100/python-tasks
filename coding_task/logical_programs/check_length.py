
# Write a function named check_length that takes a string as input and:
# Prints the length of the string. Checks if the length is more than 5 characters. 
# If yes, print: "Long string" If not, print: "Short string"

def check_length(size):
    print("Length of the string is: " , len(size))
    if len(size) > 5:
        print("Long string")
    else:
        print("Short string")

check_length("siddarth")


# Write a function called show_name_parts(name) that does the following:
# Prints the first character of the name.
# Prints the last character of the name.
# Prints the first 3 characters.
# Prints the last 3 characters.

def show_name_parts(name):
    print("Answer is : ", name[0])
    print("Answer is : ", name[-1])
    print("Answer is : ", name[0:3])
    print("Answer is : ", name[-3:])
show_name_parts("siddarth")


# Write a function check_keyword that takes a string as input.
# If the string contains the word "python", print "Python found!".
# Else, print "Not found".

def check_keyword(name):
    if "python" in name:
        print("Python found!")
    else:
        print("Python not found")

check_keyword("i love ")

