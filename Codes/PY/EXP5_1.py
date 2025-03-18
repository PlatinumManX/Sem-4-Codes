class employee:
    count=0
    def __init__(self,id):
        self.id=id
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def getid(self):
        return self.id
    @classmethod
    def setempcount(cls):
        employee.count=employee.count+1
n=int(input("Enter the Number of Employees: "))
e=[]
for i in range(n):
    eobj=employee(i+1)
    str=input("Enter Name: ")
    eobj.setname(str)
    elist=[]
    elist.append(eobj.getid())
    elist.append(eobj.getname())
    eobj.setempcount()
    e.append(elist)
for i in e:
    print(i)
print("Total Employees: ",len(e))
