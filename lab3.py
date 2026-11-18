top_name = ""
for roll, data in students.items():
    if data[1] > highest:
        highest = data[1]
        top_name = data[0]
print("\nhighest marks student:", top_name)
print("highest marks:", highest)
total = 0
for data in students.values():
    total = total + data[1]
average = total / len(students)
print("class average:", average)
count = 0
for data in students.values():
    if get_result(data[1]) == "Pass":
        count = count + 1
print("total passed students:", count)
with open("marks.txt", "w") as file:
    for roll, data in students.items():
        name = data[0]
        marks = data[1]
        result = get_result(marks)
        file.write(f"{roll}, {name}, {marks}, {result}\n")
with open("marks.txt", "a") as file:
    file.write(f"Class Average: {average}\n")
print("\n...file content........\n")
with open("marks.txt", "r") as file:
    content = file.read()
    print(content)