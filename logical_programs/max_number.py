# print max value

def max_number(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
         
    print("The max value is : ", max_value)
    
max_number([1,7,8])