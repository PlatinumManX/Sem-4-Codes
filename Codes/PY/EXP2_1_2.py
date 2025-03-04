import array
num = array.array('i',[])
n=int(input("Enter the Number of Elements: "))
for i in range(n):
      x=int(input('Enter Element Numbers[{}]: '.format(i)))
      num.append(x)
print("Array Before Appending is:- ",end='')
for i in num:
    print(i,'\t',end='')
app=int(input("\nEnter the Number to Append: "))
num.append(app)
print("Array After Appending is:- ",end='')
for i in num:
        print(i,'\t',end='')
