
# Q. Word Frequency Counter

'''
Task: Take a sentence as input from the user.
Count how many times each word appears.
Print the word along with its count.
'''

def word_counter():
    sentence = input("Enter the sentence here: ")
    print("Sentence you entered: ", sentence)

    x = sentence.split()
    print(x)

    word_count = {}

    for word in x:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(word_count)

word_counter()
