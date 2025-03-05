from collections import deque

class DequeOperations:
    def __init__(dq):
        dq.deque=deque()
    def add_front(dq,data):
        dq.deque.appendleft(data)
        print("{} added to the front".format(data))
    def remove_front(dq):
        if dq.deque is None:
            print("Deque is Empty")
        else:
            print("Removed {} from the Front".format(dq.deque.popleft()))
    def add_rear(dq,data):
        dq.deque.append(data)
        print("{} added to the rear".format(data))
    def remove_rear(dq):
        if dq.deque is None:
            print("Deque is Empty")
        else:
            print("Removed {} from the rear".format(dq.deque.pop()))
    def search_element(dq,key):
        for i in range(len(dq.deque)):
            if key==dq.deque[i]:
                print("Element {} found at Index {}".format(key,i))
            else:
                print("Element Not Found")
    def display(dq):
        if dq.deque is None:
            print("Deque is Empty")
        else:
            print("Deque Elements:",list(dq.deque))

dq=DequeOperations()
print("Ahmed Ansari")
while True:
    print('''1.Add Element at Front
2.Remove Element from Front
3.Add Element from Front
4.Remove Element from Rear
5.Search for an Element
6.Display
7.Exit''')
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        data=int(input("Enter Data: "))
        dq.add_front(data)
    elif choice==2:
        dq.remove_front()
    elif choice==3:
        data=int(input("Enter Data: "))
        dq.add_rear(data)
    elif choice==4:
        dq.remove_rear()
    elif choice==5:
        key=int(input("Enter the Element to be Searched: "))
        dq.search_element(key)
    elif choice==6:
        dq.display()
    elif choice==7:
        print("Exiting...")
        break
    else:
        print("Invalid Input")
