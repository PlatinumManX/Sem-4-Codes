class Node:
    def __init__(node,data):
        node.data=data
        node.next=None
class LinkedList:
    def __init__(node):
        node.head=None
    def display(node):
        print("The Linked List is:", end=" ")
        temp=node.head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()
    def insert_begin(node,data):
        newnode=Node(data)
        newnode.next=node.head
        node.head=newnode
    def insert_end(node,data):
        newnode=Node(data)
        if node.head is None:
            node.head=newnode
            return
        temp=node.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
    def insert_position(node,data,pos):
        newnode=Node(data)
        if pos==0:
            node.insert_begin(data)
            return
        temp=node.head
        for i in range(pos-1):
            if temp is None:
                print("Invalid Position")
                return
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    def delete_begin(node):
        if node.head is None:
            print("Linked List is Empty")
            return
        node.head=node.head.next
    def delete_end(node):
        if node.head is None:
            print("Linked List is Empty")
            return
        if node.head.next is None:
            node.head=None
            return
        temp=node.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def delete_position(node,pos):
        if node.head is None:
            print("Linked List is Empty")
            return
        if pos==0:
            node.head=node.head.next
            return
        temp=node.head
        for i in range(pos-1):
            if temp.next is None:
                print("Invalid Position")
                return
            temp=temp.next
        if temp.next is None:
            print("Invalid Position")
            return
        temp.next=temp.next.next
    def delete_element(node,key):
        temp=node.head
        if temp and temp.data==key:
            node.head=temp.next
            return
        prev=None
        while temp and temp.data!=key:
            prev=temp
            temp=temp.next
        if temp is None:
            print("Element Not Found")
            return
        prev.next=temp.next
    def search(node,key):
        temp=node.head
        index=0
        while temp:
            if temp.data==key:
                print("Element {} found at index {}".format(key,index))
                return
            temp=temp.next
            index=index+1
        print("Element Not Found")
    def replace(node,index,newdata):
        temp=node.head
        for i in range(index):
            if temp is None:
                print("Invalid Index")
                return
            temp=temp.next
        if temp is not None:
            temp.data=newdata
        else:
            print("Invalid Index")
    def forward(node):
        node.display()
    def reverse(node):
        def _reverse(node):
            if node is None:
                return
            _reverse(node.next)
            print(node.data, end=" ")
        _reverse(node.head)
        print()
    def insert_after(node,key,data):
        temp=node.head
        while temp and temp.data!=key:
            temp=temp.next
        if temp is None:
            print("Element Not Found")
            return
        newnode=Node(data)
        newnode.next=temp.next
        temp.next=newnode
ll=LinkedList()
print("Ahmed Ansari")
while True:
    print('''1.Display List
2.Insert At Beginning
3.Insert At End
4.Insert At Position
5.Insert After An Element
6.Delete From Beginning
7.Delete From End
8.Delete At Position
9.Delete An Element
10.Search An Element
11.Replace Element At A Specified Index
12.Forward Traversal
13.Reverse Traversal
14.Exit''')
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        ll.display()
    elif choice==2:
        data=int(input("Enter Data: "))
        ll.insert_begin(data)
    elif choice==3:
        data=int(input("Enter Data: "))
        ll.insert_end(data)
    elif choice==4:
        data=int(input("Enter Data: "))
        pos=int(input("Enter the Position: "))
        ll.insert_position(data,pos-1)
    elif choice==5:
        data=int(input("Enter Data: "))
        key=int(input("Enter Element after which to Insert: "))
        ll.insert_after(key,data)
    elif choice==6:
        ll.delete_begin()
    elif choice==7:
        ll.delete_end()
    elif choice==8:
        pos=int(input("Enter the Position: "))
        ll.delete_position(pos-1)
    elif choice==9:
        key=int(input("Enter the Element to Delete: "))
        ll.delete_element(key)
    elif choice==10:
        key=int(input("Enter the Element to Search: "))
        ll.search(key)
    elif choice==11:
        index=int(input("Enter the Index: "))
        newdata=int(input("Enter the new Value: "))
        ll.replace(index,newdata)
    elif choice==12:
        ll.forward()
    elif choice==13:
        ll.reverse()
    elif choice==14:
        print("Exiting...")
        break
    else:
        print("Invalid Input")

