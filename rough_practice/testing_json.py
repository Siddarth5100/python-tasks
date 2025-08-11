import json

with open("students.json", "r") as f:
    loaded_students = json.load(f)

print("Imported data from JSON:")
print(loaded_students)
