list=[]
n=int(input("Enter the Number of Students: "))
for i in range(n):
    t=eval(input("Enter Roll No., Name and Marks in Physics, Chemistry and Maths:-\n"))
    list.append(t)
name=(input("Enter the Name of the Student: "))
for i in range(n):
    if list[i][1] == name:
        print(list[i])
        break
else:
    print("Name Not Found")
