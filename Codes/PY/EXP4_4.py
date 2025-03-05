d1=eval(input("Enter a dictionary : "))
def display():
    print("The dictionary is ",d1)
    return
def sort():
    print(sorted(d1.items(),key=lambda t:t[0]))
    print("Sorted by keys\n")
    print(sorted(d1.items(),key=lambda t:t[1]))
    print("Sorted by value")
    return
def concat():
    d2=eval(input("Enter another dictionary : "))
    d1.update(d2)
    print("Updated dictionary is ",d1)
    return
while True:
    print('''1.DISPLAY
2.SORT
3.CONCATENATE
4.EXIT''')
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        display()
    elif choice==2:
        sort()
    elif choice==3:
        concat()
    elif choice==4:
        print("Exiting...")
        break
    else:
        print("Invalid Input")
