
def total_expense():
    user_input = input("Enter the prices separated by commas : ")   # input as a string
    print(user_input)   # to get the input printed
    prices = [int(x.strip()) for x in user_input.split(",")]    # to split into parts to create list, 
    print(prices)
    total = 0
    for price in prices:    # loop thruogh the list to calculate the sum
        total += price    
    return total            # returned the total     

grand_total = total_expense()
print(grand_total)



def calculate_total(price,quantity):
    total_cost = price * quantity
    return total_cost

total_bill = calculate_total(30,2)

print("total bill :", total_bill)

