
# Question 5: Mixed Concepts (Strings + Loops + Conditions)

'''
Task: Write a program that:
Takes a word as input, Prints each character one by one,Counts and prints how many vowels are in the word.
Finally, print the word in reverse.
'''

def count_vowels():

    vowels = ["a","e","i","o","u"]
    
    word = input("Enter a word: ")

    count = 0

    print("Characters entered : ", word)

    for letter in word:
        print(letter,end=" ")

        if letter in vowels:  
            count += 1

    print("\nTotal vowels in the word:", count) 
    print("Reverse of the word:", word[::-1])
                    
count_vowels()

