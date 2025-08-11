# objective to store book details, search/filter, update/remove entries. 

# data structure

books = {"B1001" : {"title" : "The Great Gatsby",
                    "author" : "F. Scott Fitzgerald",
                    "year" : 1925,
                    "available" : True
    },
    "B1002" : {"title" : "1984",
               "author" : "George Orwell",
               "year" : 1949,
               "available" : False

    }
}

def add_a_book():
    book_id = input("Enter the id of the book :")
    title = input("Enter the title of the book :")
    author = input("Enter name of the author :")
    year = input("Enter year :")
    available_input = input("Is available yes/no :")
    available = True if available_input == "yes" else False 
    
    books[book_id] = {"title":title, 
                      "author":author, 
                      "year":year, 
                      "available":available
}
    print("Book added successfully!")
    print(books)


add_a_book()





