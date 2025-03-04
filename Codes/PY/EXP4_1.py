list=[]
n=int(input("Enter the Number of Elements in the List: "))
print("Enter the Elements")
for i in range(n):
    temp=int(input())
    list.append(temp)
#print(list)
listeven=[]
listodd=[]
for i in range(n):
    if list[i]%2==0:
        listeven.append(list[i])
    else:
        listodd.append(list[i])
print("List containing Even Elements is:",listeven)
print("List containing Odd Elements is:",listodd)
listall=[]
listall=listeven+listodd
print("Merged List is:",listall)
listall=sorted(listall)
print("Sorted List is:",listall)
x=int(input("Enter the Number with which the First Elements is to be Updated: "))
listall[0]=x
print("List after Updating First ELements is:",listall)
mid=int(len(listall)/2)
print("Middle Element of the List is: ",listall[mid])
