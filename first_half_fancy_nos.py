
#1st half numbers

starting_num = input("Enter the number required: ")

def start_number():
    print("Number entered:", starting_num)
    count = 0

    for ph_num in range(9000000000, 9999999999):
        if str(ph_num).startswith (str(starting_num)):            
            print("The number's available is: ", str(ph_num))
            count += 1
            
            if count >=10:
                break

    print("Total numbers available: ", count)

start_number()