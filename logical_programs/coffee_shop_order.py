# coffeeshop_order

def greet():
    print("Good day")

menu = ["coffee" , "biscuit" , "samosa", "puffs"]

item_rates = {"coffee":10, "biscuit":12, "samosa":15, "puffs":20}

def get_item_name():
    for items in menu:
        print(items)
    item = input("Enter item name: ")
    return item

def coffee_shop_order():
    greet()
    print("Items availabe: ")  # items:coffee,biscuit,samosa,puffs
    
    #print(get_item_name())
    
    selected_item = get_item_name()
    
    print("You're oredered received: ", selected_item) 

    if selected_item in menu:
        qty = int(input("Enter the no.of.quantity: "))  #total amount = quantity * rate
        total_amount = qty * item_rates[selected_item]
        print("Your total amount: ", total_amount)
        
    else:
        print("Kindly enter the valid items")

coffee_shop_order()

