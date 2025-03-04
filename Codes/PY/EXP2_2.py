import array
num = array.array('i',[])
num2 = array.array('i',[])
flag=0
n=int(input("Enter the Number of Elements: "))
for i in range(n):
      x=int(input('Enter Element Numbers[{}]: '.format(i)))
      num.append(x)
print("Array Before Removing Prime Numbers is:- ",end='')
for i in num:
    print(i,'\t',end='')
for i in range(n):
    j=num[i]
    z=num[i]
    for j in range(j-1,1,-1):
        if(num[i]%j==0 and flag==0):
            num2.append(z)
            flag=1
    flag=0
print("\nArray After Removing Prime Numbers is:- ",end='')
for i in num2:
    print(i,'\t',end='')
