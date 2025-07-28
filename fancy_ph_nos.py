
# want to get input from user for suggesting fancy numbers.
# check how many variations are there, want to print ("The whole numbers which is available under required category")
# eg - 91234 if i give input it should print starting numbers: 

req_num = input("Enter the number required: ")

def fancy_numbers():
    print("Number entered :", req_num)
    count = 0
    for ph_no in range(9000000001, 9999999999):
        if str(req_num) in str(ph_no):
            print("The number's available is: ", str(ph_no))     
            count += 1
            if count >= 10:
                break

fancy_numbers()

