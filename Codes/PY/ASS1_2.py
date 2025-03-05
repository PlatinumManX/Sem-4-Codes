class stack:
    def __init__(st):
        st.stack=[]
    def push(st, data):
        st.stack.append(data)
    def pop(st):
        if len(st.stack)==0:
            print("The Stack is Empty")
            return
        return st.stack.pop()
    def top(st):
        if len(st.stack)==0:
            print("The Stack is Empty")
            return
        return st.stack[-1]
    def search(st,element):
        l=len(st.stack)
        for i in range(l):
            if st.stack[i]==element:
                print("The Element {} is Found at Index {}".format(st.stack[i],i+1))
                return
        print("The Element is Not Found")
        return
    def display(st):
        if len(st.stack)==0:
            print("The Stack is Empty")
        else:
            print("The Stack is:",st.stack[::-1])

s=stack()
print("Ahmed Ansari")
while True:
    print('''1.Push an Element
2.Pop an Element
3.Top of Stack
4.Search an Element
5.Display Stack
6.Exit''')
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        data=int(input("Enter the Data: "))
        s.push(data)
    elif choice==2:
        temp=s.pop()
        if temp is not None:
            print("Popped Element is ",temp)
    elif choice==3:
        top=s.top()
        if top is not None:
            print("Top Element is ",top)
    elif choice==4:
        element=int(input("Enter the Element to be Searched: "))
        s.search(element)
    elif choice==5:
        s.display()
    elif choice==6:
        print("Exiting...")
        break;
    else:
        print("Invalid Input")
        
