# Given the following list of numbers:
# numbers = [12, 18, 25, 30, 45, 50, 60, 77]

#Write a Python program to:
#Print only the numbers that are divisible by both 2 and 3. Store them in a new list. Calculate and print the average of that new list

def divisible_numbers():
    numbers = [12, 18, 25, 30, 45, 50, 60, 77]
    divisible_list = []

    for n in numbers:
        if n % 2 == 0 and n % 3 == 0:
            divisible_list.append(n)

    print("Numbers divisible by both 2 and 3:", divisible_list)

    if len(divisible_list) > 0:
        average = sum(divisible_list) / len(divisible_list)
        print("Average of those numbers:", average)
    else:
        print("No numbers divisible by both 2 and 3.")

divisible_numbers()
