import json    # to import json module, without doing this python will not understand what it is 
import os    # to check if that .json file exist

json_file_path = "coding_task/library_management"    # where data is saved

# Library Book Management System 
# Goal: Create a program to manage library books, track borrowers, and calculate usage reports

library = {
    "books" : {
        "B1000" : {"title" : "python basics" , "author" : "john" , "copies" : 3}
    },
    "users" : {
        "U0001" : {
            "name" : "siddhu",
            "borrowed books" : ["B1000", "B10001"]
        }
    }
}

print(library)

# function to add books

def add_books(book_id,title,author,copies):
    library["books"][book_id] = {
    "title" : title , "author" : author , "copies" : copies}
    print("Book successfully added")
    

add_books("B1001","est","helo",10)

print(library["books"])

def register_user(user_id,name,role):
    library["users"][user_id] = {
        "name" : name,
        "role" : role
    }

register_user("1","s","d")

with open("coding_task/library_data.json", "w") as lib:
    json.dump(library, lib, indent =4)



