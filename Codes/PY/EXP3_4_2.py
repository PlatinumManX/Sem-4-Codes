from EXP3_4_1 import *
numbers=[]
list=input("Enter the Numbers: ")
numbers.extend(map(int, list.split()))
while True:
    choice=int(input('''1.Summation of All Elements
2.Product of All Elements
3.Summation of Elements at Even Indices
4.Add Elements in the List
5.Exit
Enter Your Choice: '''))
    if choice == 1:
        sum=summation(numbers)
        print("The Summation of All Elements is: {}".format(sum))
    elif choice == 2:
        pro=product(numbers)
        print("Product of All Elements is: {}".format(pro))
    elif choice == 3:
        even=sumeven(numbers)
        print("The Summation of Elements at Even Indices is: {}".format(even))
    elif choice == 4:
        num=int(input("Enter the Number to Append: "))
        numbers=app(numbers,num)
        print("The Appended List is:-")
        for i in numbers:
            print(i,end=' ')
        print()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
