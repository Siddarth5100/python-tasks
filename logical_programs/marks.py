
marks = int(input("Enter the marks :"))
print("Marks entered :",marks)

if marks >= 80:
    print("Grade A")
elif marks >= 50:
    print("Grade B")
else:
    print("Grade C")

for i in range(1,11):
    print(i)
    if i == 5:
        continue
    if i == 8:
        break
print(i)