def add(*a):
    sum=0
    for i in a:
        sum=sum+i
    print("Addition of the Numbers is {}".format(sum))
def subtract(*a):
    sum=a[0]
    for i in a[1:]:
        sum=sum-i
    print("Subtraction of the Numbers is {}".format(sum))
def multiply(*a):
    mul=1
    for i in a[::1]:
        mul=mul*i
    print("Multiplication of the Numbers is {}".format(mul))
def divide(*a):
    div=a[0]
    for i in a[1::]:
        div=div/i
    print("Division of the Numbers is {}".format(div))
while True:
    choice=int(input('''1.Addition
2.Subtraction
3.Multiplication
4.Division
Enter Your Choice: '''))
    if(choice==1):
        numbers=list(map(int,(input("Entet the Numbers:- ").split())))
        add(*numbers)
    elif(choice==2):
        numbers=list(map(int,(input("Entet the Numbers:- ").split())))
        subtract(*numbers)
    elif(choice==3):
        numbers=list(map(int,(input("Entet the Numbers:- ").split())))
        multiply(*numbers)
    elif(choice==4):
        numbers=list(map(int,(input("Entet the Numbers:- ").split())))
        divide(*numbers)
    else:
        print("Invalid Input")
        break
