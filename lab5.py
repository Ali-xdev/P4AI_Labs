marks1=float(input("enter your marks1:"))
marks2=float(input("enter your marks2:"))
marks3=float(input("enter your marks3:"))
def student():
    name=input("enter your name:")
    print("name",name)
def total_marks():
    total=marks1+marks2+marks3
    print("total",total)
def percentage():
    percentage=(total/300)*100
    return percentage
    print("percentage",percentage)
    PASS_MARKS=50
def grade():
    print("grade")
    if percentage<90:
        grade="A"
    elif percentage<80:
        grade="B"
    elif percentage<70:
        grade="C"
    elif percentage<60:
        grade ="D"
    else:
        grade="F"
def result():
    print("grade",grade)
    print("percentage",percentage)
    print("result",result)
    if(percentage>=50):
        print("pass")
    elif(percentage<50):
        print("fail")
student()
total_marks()
percentage()
grade()
result()