class Queue:
    def __init__(q):
        q.queue=[]
    def insert(q,data):
        q.queue.append(data)
    def remove(q):
        if len(q.queue)==0:
            print("Queue Underflow")
        else:
            temp=q.queue.pop(0)
            print("Deleted Element is: ",temp)
    def search(q,key):
        for i in range(len(q.queue)):
            if key==q.queue[i]:
                print("Element {} found at Position {}".format(key,i))
                return
        print("Element Not Found")
        return
    def display(q):
        if len(q.queue)==0:
            print("Queue Underflow")
        else:
            print("Queue Elements are:",end=" ")
            for i in range(len(q.queue)):
                print(q.queue[i],end=" ")
            print()

q=Queue()
print("Ahmed Ansari")
while True:
    print('''1.Insert an Element
2.Remove an Element
3.Search an Element
4.Display Queue
5.Exit''')
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        data=int(input("Enter Data: "))
        q.insert(data)
    elif choice==2:
        q.remove()
    elif choice==3:
        key=int(input("Enter the Element to be Searched: "))
        q.search(key)
    elif choice==4:
        q.display()
    elif choice==5:
        print("Exiting...")
        break;
    else:
        print("Invalid Input")
    
