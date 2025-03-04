import array
num = array.array('i',[])
n=int(input("Enter the Number of Elements in the Array: "))
for i in range(n):
      x=int(input('Enter Element Numbers[{}]: '.format(i)))
      num.append(x)
print("Array Before Removing is:- ",end='')
for i in num:
    print(i,'\t',end='')
rem=int(input("\nEnter the Index of the Element to be Removed: "))
num.pop(rem)
print("Array After Removing is:- ",end='')
for i in num:
        print(i,'\t',end='')
