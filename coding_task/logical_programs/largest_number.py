
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
