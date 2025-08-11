
name = input("Enter your name here: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
print("My name is : ", name)
print("My age is: ", age)
print("My address is: ", address)


a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))
multiply = (a * b * c)
add = (a + b + c)
divide = (multiply/add)
print("The value is: ", divide)


name = input("Enter name: ")
score = int(input("Enter score for 100: "))
department = input("Enter department: ")
divide = score / 10
print("your score is: ", divide, "/10")



def user_info():
    print("Name: siddhu")
    print("City: Coimbatore")

user_info()


def check_even():
    number_1 = int(input("Enter the number: "))
    if number_1 % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")

check_even()


for i in range(1,6):
    print(i)

word = input("Enter the word:")
print(word)

for letters in word:
    print(letters)

word = input("Enter a word: ")
count = 0
for letter in word:
    count += 1
    
print("Total characters: ", count)
print("Total no is:", count)
 


words = input("Enter here: ")
digits = ["0","1","2","3","4","5","6","7","8","9"]
total = 0 

print("Digits found: ", end="")

 # input 123qw

for i in words:
    if i in digits:
        print(i, end=" ")
        total += 1

print("\nTotal number of digits:", total)



sen = input("Enter a sentence with digits: ")
count_char = 0
digits = ["1","2","3","4","5","6","7","8","9","0"]
total = 0

for i in sen:
    if i in digits:
        total += 1

print("The total digits is: ", total)










