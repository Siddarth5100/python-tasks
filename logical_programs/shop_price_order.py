
# Get Top Three Items in a Shop
# Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
'''
Expected Output:
item4 55
item1 45.5
item3 41.3
'''

shop = {"shampoo":120, "toothpaste":50, "soap":30, "perfume":500, "facewash":200, "lotion":150}

def price_from_top():
    items = list(shop.items())

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] < items[j][1]:
                items[i], items[j] = items[j], items[i]

    print(items[0][0], items[0][1])
    print(items[1][0], items[1][1])
    print(items[2][0], items[2][1])

price_from_top()
