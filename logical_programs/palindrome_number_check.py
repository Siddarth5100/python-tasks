#task_1 : Write a program that checks whether a given number is a palindrome.

def check_palindrome(number):
    print("Number you entered:", number)
    reversed_number = str(number)[::-1]
    print("Reversed to:" , reversed_number)
   
    if str(number) == reversed_number:
        print("It is a palidrome!")
    else:
        print("It is not a palindrome") 

check_palindrome(152510)


