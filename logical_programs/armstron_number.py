def armstrongnumber(a):
    print("Number you entered =", a)

    num_str = str(a)
    n = len(num_str)
    print("Number of digits =", n)

    total = 0
    for digit in num_str:
        total += int(digit) ** n

    if total == a:
        print("It is an Armstrong number!")
    else:
        print("Not an Armstrong number")


armstrongnumber(123)
