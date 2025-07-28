
# Given a list of numbers: numbers = [10, 25, 30, 47, 50, 63]
# Write a program to, Print only even numbers from the list. Print the count of even numbers at the end

def even_numbers():
    numbers = [10, 25, 30, 47, 50, 63]
    even_list = []
    count = 0

    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
            count += 1

    print("Even numbers are:", even_list)
    print("Total count of even numbers:", count)

even_numbers()

