'''

# Question 1: Create and print a dictionary

# Create a dictionary that stores the following fruit prices:
#    Apple: 30
#    Banana: 10
#    Mango: 50
# Print the entire dictionary.

# Ans:

def create_print():

    this_dict = {"Apple":30, "Banana":10, "Mango":50}
    #this_dict = dict(Apple=30, Banana = 10, Mango = 50)    dict() constructor - to make dictionary
    
    print(this_dict)
    print(this_dict["Mango"])

create_print()



# Question 3: Add a new item to the dictionary

# Start with: fruits = {"Apple": 30, "Banana": 10, "Mango": 50}
# Task: Add "Orange": 40 to the dictionary and print the updated dictionary.
 
# Ans:

fruits = {"Apple": 30, "Banana": 10, "Mango": 50}

fruits["Orange"] = 40
print(fruits)


# Question 4: Update the value of an existing key
# Given: fruits = {"Apple": 30, "Banana": 10, "Mango": 50}
# Task: Update the price of "Banana" to 15 and print the updated dictionary.

# Ans:

fruits = {"Apple": 30, "Banana": 10, "Mango": 50}

fruits.update({"Banana": 15})
print(fruits)

# for loop practice

fruits = {"Apple": 30, "Banana": 15, "Mango": 50, "Orange": 40}

for x in fruits:
    print(x)

for x in fruits:
    print(fruits[x])

for x in fruits.values():
    print(x)

for x in fruits.keys():
    print(x)

for x,y in fruits.items():
    print(x,y)


# Question 5: Loop through a dictionary

# Given: fruits = {"Apple": 30, "Banana": 15, "Mango": 50, "Orange": 40}
# Task: Print each fruit and its price in this format: Use a for loop to do this.
# Apple costs 30
# Banana costs 15
# ...

# Ans:

fruits = {"Apple": 30, "Banana": 15, "Mango": 50, "Orange": 40}

def fruits_price():
    for name,price in fruits.items():
        print(name, "costs", price)

fruits_price()


# Question 6: Check if a key exists in the dictionary

# Given: fruits = {"Apple": 30, "Banana": 15, "Mango": 50, "Orange": 40}

# Task: Check if "Pineapple" exists in the dictionary.
# If it exists, print the price. If it doesn't, print "Pineapple not found".

# Ans:

fruits = {"Apple": 30, "Banana": 15, "Mango": 50, "Pineapple": 40}

def checking_items():
    for x in fruits:
        print(x)
    
    if "Pineapple" in fruits: 
        print("Pineple is availabe. Price is :", fruits["Pineapple"])
    else:
        print("Pineapple is not available")

checking_items()


# Question 7: Print fruits priced above 30

# Given: fruits = {"Apple": 30, "Banana": 15, "Mango": 50, "Orange": 40}
# Task: Loop through the dictionary and print only the fruits that cost more than 30.

# Ans: 

fruits = {"Apple": 30, "Banana": 15, "Mango": 50, "Orange": 40}


def fruits_price():
    for price in fruits.values():
        
        if price >= 30:
            print(price())
fruits_price()


def fruits_price():
    for fruit, price in fruits.items():
        if price > 30:
            print(fruit ,"costs" ,price )

fruits_price()


# Question 8: Count how many fruits cost less than or equal to 30

# Given: fruits = {"Apple": 30, "Banana": 15, "Mango": 50, "Orange": 40}
# Task: Count how many fruits have a price ≤ 30 and print that count.

fruits = {"Apple": 30, "Banana": 15, "Mango": 50, "Orange": 40}

def price_count():

    count = 0
   
    for fruit,price in fruits.items():    
        if price <= 30:
            count += 1
    print("Number of fruits costing 30 or less: ", count)

price_count()

'''
    

