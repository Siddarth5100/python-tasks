# Ask the user to enter a word.
# Then print only the vowels (a, e, i, o, u) from that word using a for loop.

word = input("Enter a word : ")
vowels = ["a","e","i","o","u"]
count = 0

for letter in word:
    if letter in vowels:
        print(letter)
        count +=1 # count = count + 1 