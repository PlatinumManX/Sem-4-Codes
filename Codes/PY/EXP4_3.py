A=set(map(int, input("Enter the Elements of Set A separated by spaces: ").split()))
B=set(map(int, input("Enter the Elements of Set B separated by spaces: ").split()))
print("Set A:",A)
print("Set B:",B)
while True:
    choice=int(input('''1.Intersection
2.Union
3.Set Difference
4.Symmetric Difference
5.Exit
Enter Your Choice: '''))
    if choice==1:
        print("Intersection of A and B is",(A&B))
    elif choice==2:
        print("Union of A and B is",(A|B))
    elif choice==3:
        print("Set Difference of A and B is",(A-B))
    elif choice==4:
        print("Symmetric Difference of A and B is",(A^B))
    elif choice==5:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
 
