from Details.Employee.profile import Profile
from Details.Employee.qualification import Qualification
from Details.Account.salary import Salary

name=input("Enter Employee Name: ")
age=int(input("Enter Age: "))
dob=input("Enter Date of Birth (DD/MM/YYYY): ")
degree=input("Enter Degree: ")
experience=int(input("Enter Years of Experience: "))
basic=int(input("Enter Basic Salary: "))
hra=int(input("Enter HRA: "))
pf=int(input("Enter PF: "))

emp_profile=Profile(name,age,dob)
emp_qualification=Qualification(degree, experience)
emp_salary=Salary(basic, hra, pf)

print("\nEmployee Details:-")
print(emp_profile.display())
print(emp_qualification.display())
print(emp_salary.display())
