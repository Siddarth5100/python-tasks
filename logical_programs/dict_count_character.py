
# Q Count Character Frequency (Ignore Spaces)
'''
Task: Take a sentence as input from the user.
Count how many times each character appears, excluding spaces.
Store the result in a dictionary and print it.
'''

def character_counter():
    sentence = input("Enter the sentence here: ")
    print("Sentence entered: ", sentence)

    char_count= {}

    for char in sentence:
        if char != " ":
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    print("Answer is: ", char_count)

character_counter()


