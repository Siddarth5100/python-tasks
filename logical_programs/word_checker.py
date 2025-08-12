
# **Write a function** that checks if the word `"code"` is present in a sentence.
# If found, print `"Code is present!"`
# If not, print `"Code not found." You can name the function `check_code_word(sentence)`


def word_check(word):
    if "code" in word:
        print("Code is present")
    else:
        print("code not found")

word_check(" is in wordpad")


# Write a function to check if a name starts with the letter "S" (case-insensitive).
# If yes, print "Name starts with S" Else, print "Name doesn't start with S" Function name: check_name_start(name)


def check_letter(letter):
    #if letter.startswith("S"):
    if letter.startswith("S"):
        print("Name starts with S")
    else:
        print("Name doesn't start with S")

check_letter("Sddart")

# Count how many digits are in a word
# Example: If input is: abc123def456. It should print:


digits = input("Enter here: ")
total = 0 

for i in digits:
    if i.isdigit():
        print(i)
        total += 1

print("Total number of digits: ", total)
