# Write a program to count how many uppercase and lowercase letters are present in a word.

word = input("Enter words here: ")
upper_count = 0
lower_count = 0 

for i in word:
    if i.isupper():
        upper_count += 1
    if i.islower():
        lower_count += 1


print("Uppercase letters count:", upper_count)
print("Lowercase letters count:", lower_count)