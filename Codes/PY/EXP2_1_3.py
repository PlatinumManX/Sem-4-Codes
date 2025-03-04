import array
num = array.array('i',[])
n=int(input("Enter the Number of Elements: "))
for i in range(n):
      x=int(input('Enter Element Numbers[{}]: '.format(i)))
      num.append(x)
print("Array Before Reversing is:- ",end='')
for i in num:
    print(i,'\t',end='')
num2=num[::-1]
print("\nArray After Reversing is:- ",end='')
for i in num2:
        print(i,'\t',end='')
