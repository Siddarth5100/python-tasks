#task_2 : Write a program that calculates the sum of all digits in a number.

def add(a):
    total = 0 
    for digit in str(a):
        total += int(digit)
    print("Sum of digits:", total)

add(12121212)

