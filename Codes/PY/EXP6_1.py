class Fail(Exception):
    def __init__(self, message="Marks are less than 40"):
        self.message=message
        super().__init__(self.message)
class Student:
    def __init__(self, rno, name, marks):
        self.rno=rno
        self.name=name
        self.marks=marks
    def display(self):
        try:
            if self.marks<40:
                raise Fail()
            print("Roll No: {}\nName: {}\nMarks: {}".format(self.rno,self.name,self.marks))
        except Fail as e:
            print("Roll No: {}\nName: {}\nMarks: {}\n{}".format(self.rno,self.name,self.marks,e))

n=int(input("Enter the Number of Students: "))
list=[]
for i in range(n):
    print("Enter Details of Student {}".format(i+1))
    rno=int(input("Enter Roll No: "))
    name=input("Enter Name: ")
    marks=int(input("Enter Marks: "))
    list.append(Student(rno, name, marks))
print("\nStudent Details:-")
i=1
for student in list:
    print("Student {}:-".format(i))
    student.display()
    print()
    i=i+1
