n=int(input("Enter the Value of n:"))
print("0 1 ",end="")
j=0
k=1
for i in range(1,n-1,1):
    print(j+k,end=" ")
    temp=k
    k=j+k
    j=temp
