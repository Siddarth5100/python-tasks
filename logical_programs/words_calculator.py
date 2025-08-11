
sentence = input("Enter a sentence: ")
a = sentence.split()
total = 0

for word in a:
    total += 1

print("Total number of words:", len(a))
