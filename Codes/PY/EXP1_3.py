num1=int(input("Enter a Number:"))
num2=int(input("Enter a Number:"))
choice=int(input('''1.Addition
2.Subtraction
3.Multiplication
4.Division
Enter Your Choice:'''))
if choice==1:
    print("Addition of {} and {} is {}".format(num1,num2,num1+num2))
elif choice==2:
    print("Subtraction of {} and {} is {}".format(num1,num2,num1-num2))
elif choice==3:
    print("Multiplication of %d and %d is %d"%(num1,num2,num1*num2))
elif choice==4:
    print("Division of %d and %d is %d"%(num1,num2,num1/num2))
else:
    print("Invalid Choice")
