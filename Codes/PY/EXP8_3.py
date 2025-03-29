import os
current_dir=os.getcwd()
print("Current Directory: ",current_dir)
print('''1.Create a Directory
2.Create Nested Directories
3.Delete a Directory
4.Delete Nested Directories
5.Change Current Directory
6.Exit''')
while True:
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        single_dir=input("Enter Name of Single Directory to be Created: ")
        os.mkdir(single_dir)
        print("Directory {} Created".format(single_dir))
    elif choice==2:
        nested_dir=input("Enter Name of Nested Directories to be Created in the form of 'Parent/Child': ")
        os.makedirs(nested_dir)
        print("Nested Directories {} Created".format(nested_dir))
    elif choice==3:
        single_dir=input("Enter Name of Single Directory to be Deleted: ")
        os.rmdir(single_dir)
        print("Directory {} Deleted".format(single_dir))
    elif choice==4:
        nested_dir=input("Enter Name of Nested Directories to be Deleted in the form of 'Parent/Child': ")
        os.removedirs(nested_dir)
        print("Nested Directories {} Deleted".format(nested_dir))
    elif choice==5:
        dir=input("Enter the Directory to be Changed to: ")
        os.chdir(dir)
        print("Changed to ",os.getcwd())
    elif choice==6:
        print("Exiting...")
        break;
    else:
        print("Invalid Choice")
