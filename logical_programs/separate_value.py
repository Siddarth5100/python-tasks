# separate value from the list based on the type.

def separate_value():
    a = []  # to store integers
    b = []  # to store strings
    c = []  # to store floats
    values = [1, 2, "apple", 3.10, "kiwi"]

    for item in values:
        if type(item) == int:
            a.append(item)
        elif type(item) == str:
            b.append(item)
        elif type(item) == float:
            c.append(item)

    print("Integers:", a)
    print("Strings:", b)
    print("Floats:", c)

separate_value()



