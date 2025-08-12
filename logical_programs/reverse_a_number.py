#task_3 : Write a program to reverse a number.
#Goal for this : input number should get reversed, 

def reverse_number(number):
    print("Number you entered:", number)
    rev_no = str(number)[::-1]
    print("The number is", rev_no)
    
reverse_number(500)
