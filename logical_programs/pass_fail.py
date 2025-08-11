def check_pass_fail():
    num = int(input("Enter the number: "))
    if num > 100:
       print("Invalid input. Marks should be out of 100.")
    elif num >= 40:
         print("You are pass")
    else:
        print("You are fail")


check_pass_fail()