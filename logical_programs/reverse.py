def reverse_letter(word):
    if word == word[::-1]:
        print(word)
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

reverse_letter("siddhu")