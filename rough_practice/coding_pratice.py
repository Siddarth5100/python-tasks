'''

name = input("Enter your name: ") # This line name is variable that store the input value we are getting for that, input is a function that used to get input from user "" insdie the quatation that is a string used to display the message
age = input("Enter your age: ") # This line age is variable that store the input value, inout fun for getting the inout,
print("My name is" , name , "and I'm" , age , "years old") # This line print function in uesd to print the output, name & age data took from the variable name and age and used here to get the datas stored in that variable

x = 10 # this is variable, x is variable name 10 is variable value stored in x 
total = 5+x # this is variable, total is variable name here 5 is the varible value that added to x variable, so that we will get value that stored in x
print("Answer is:", total) # here print fun is used, that print what we entered inside and we added the varialbe(total) what we req


name = input("Enter your name: ")  # string input for name
age = int(input("Enter your age: "))  # converting age to int
height = float(input("Enter your height: "))  # converting height to float
student = input("Are you a student? yes/no: ")  # input to check if student

is_student = student == "yes"  # convert string answer to bool
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


is_raining = input("Is it raining outside? \n yes/no: ") # variable for storing the inout from user

if is_raining == "yes":                                   # function for checking the value of user with our datat
    print("Take an umberlla!")                          # if statement true print this
else:                                                   # Else fun
    print("Enjoy the sunshine!")                        # Else print this one

    
    Takes the user's age as input (integer)

Checks if the user is 18 or older

If yes, print: "Eligible to vote"

Else, print: "Not eligible to vote"

Add a comment to each line


age = int(input("Enter your age: ")) # variable age to store input from user
if age >= 18:                        # if function, age varible is used to get the user value, >= for comparrision, 
    print("Eligible to vote!")       # for printing the msg is it is true
else:                                # else funtion
    print("Your are not elegible to vote!")     #to print if the statement is false


user_pwd = input("Enter your password: ") #user_pwd is varible to store the input for geeting the values from user. "" string used to display the ques to user

if user_pwd == "admin123":      # if function is used to compare the values(what we have and user input) 
    print("Access granted!")    # print fun to print the output if it is true
else:                           # else fun
    print("Access denied!")     # printfun to print the outout if it is false

    
first_name = input("Enter your First name: ") # first_name is a variable to store data getting from the user, input() fun used to get  input from user, "" used to enter the messges to display
last_name = input("Enter your Last name: ") # last_name is a variable to store data getting from the user, input() fun used to get  input from user, "" used to enter the messges to display
full_name = first_name + " " +  last_name # full_name is variable, that stores what we are adding, "" for giving gap inbtwn
print("Hello, my name is ",full_name) #used to print the output



sentence = input("Enter a sentence: ") #sentence is a variable, input functions used.
print(len(sentence))                   #print fun, len fun is used to check the length of the value
print(sentence.upper())                #print fun, .upper() fun is used to change the value
print(sentence.lower())                #print fun, .lower() fun is used to change the value



user_name = input("Enter the full name: ") # username is varible to store data from user, input function
print(user_name.title())                   # print function titlce fun used to make the starting letter caps.
print(user_name [:3])                      # print fun, [] slice syntax used to slice



sentence = input("Enter a sentence: ")          # sentence is variable, used input() fun, 
print(sentence)                                 # print function used and called sentence data
print("Title case :", sentence.title())         # print fun, title fun for making the sentence titled
print("Lenght : ", len(sentence))               # print fun, len fun 
print("Last five letters is: ", sentence[-5:])  # print fun, slicing sentence []
print("Uppercase : ", sentence.upper())         # print and upper fun


def greet_user(name):                           #def for defining the function, greet_user fun name created by us(name) parametrers for the function : indicates the block started 
    print("Hello,", name , "welcome back")      #print function name called inside the string
    
greet_user("Siddhu")                            #call function by using greet_user, "" inside we passed arguments


a = 10
b = 20

a,b = b,a

print(a)
print(b)



def square_number(number): # def defining the fun, square_number = variable, () parameters : start of the block
    num = number * number  # num new variable to store the squ, * oprators to calculate
    return(num)             # return function calling num for the input value
    

square_number(4) #calling the function with () arguments


def add_numbers(num_1, num_2):
    
    total = num_1 + num_2
    print("The answer is: ", total)

add_numbers(2,3)


def greet_person(name):  #def, defining we are creating new function, name parameters
    print("Hello," , name,"!", "Hope you're doing well" )  #print function, msg to display & called name 

greet_person("Siddhu") # greet_person(), used to call the function, inside brackets argument valu passed
    

def multiply_names(number_1, number_2):
    return "Your answer is: " + str(number_1 * number_2) 

print(multiply_names(3,6))


def get_initials(name):
    return "Your answer is: " + name.title()

print(get_initials("siddhu jc"))


Q2.
Write a correct program that:

    Uses a variable called name

    Stores your name inside it

    Prints: Hi, [your name]

👉 Use proper syntax, spacing, and print statement.

#ans

name = "Siddhu"
print("Hi", name)


Q5.
Write a correct print statement that includes:

    A tab space between two words

    A line break after

print("Hello \tSiddhu \nWelcome")

Great! 💪 Here are **2 high-difficulty mixed-debug questions** — combining **syntax**, **indentation**, **escape characters**, and **function structure**. Solve each fully. Let me know if you want a clue.

---

### 🔍 **Q1: Complex Debug - Travel Planner**

```python
# Travel info
def TravelPlan()
    Destination = "Goa"
    print("Destination:\t", destination)
    print("Status: \nBooked")
    
Travelplan()
```

---

### 🔍 **Q2: Complex Debug - User Greeting**


# Booking Info
def booking_info():
    location = "Pondicherry"
    status = "Confirmed"
    print("Location:\t", location)
    print("Status:\n", status)

booking_info()


,,, 

'''