
# ques : Write a program that takes a number as input and checks:
# If the number is positive, print "Positive number. If it's zero, print "Zero" . If it's negative, print "Negative number"

def number_check():
    number = int(input("Enter the number = "))
    if number > 0:
        print("Number is positive!")
    elif number == 0:
        print("zero")
    else:
        print("Negative digit")    

number_check()