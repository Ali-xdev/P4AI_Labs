#function check

"""def is_valid_password(password):
    return len(password) >= 8
password = "python123"
if is_valid_password(password):
    print("password is valid")
else:
    print("password is not valid")"""

#a word starts with a letter A

"""def starts_with_a(word):
    return word.lower().startswith("a")
word = "Artificial"
print("starts with A",starts_with_a(word))"""

#average is passing score

"""def calculate_average(mark1, mark2, mark3):
  average = (mark1 + mark2 + mark3) /3
  return average
def is_passed(average):
    return average >= 50
average = calculate_average(70, 65, 80)
passed = is_passed(average)
print("average", average)"""

#activity


def calculate_average(mark1 , mark2, mark3):
    average = (mark1 + mark2 + mark3) /3
    return average
def is_passed(average):
    return average>=50
average = calculate_average(90 , 60, 80)
passed = is_passed(average)
print("average", average)
def get_grade(average):
    if average >= 80:
        message = "grade A."
    elif average >= 70:
        message = "grade B."
    elif average >= 60:
        message = "grade C."
    elif average >= 50:
        message = "grade D."
    elif average >= 50:
        message = ("grade E")
    else:
        message = "grade failed."
    return message
def student_report(name, average, grade ):
    return name, average, grade, average >= 50
average = calculate_average(90, 60, 80)
passed = is_passed(average)
message = get_grade(average)
report = student_report("meenu", average, message)
print("student report", report)