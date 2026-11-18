total=0
count=0
records=int(input("enter number of records(-1 is entered):"))
while records!=1:
    total+=count
    count+=1
    records=int(input("enter number of records(-1 is entered):"))
    subjects=["programming","mathematics","artificial intelligence"]
    for subject in subjects:
      print("subject:", subjects)
    for marks in range(0, 3):
      marks1 = int(input("enter marks1:"))
    marks2= int(input("enter marks2:"))
    marks3= int(input("enter marks3:"))
    if count>0:
        total=marks1+marks2+marks3
        average=total/count
        print("average:", average)
        print("total marks:", total)