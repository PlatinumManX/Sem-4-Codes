import array
num = array.array('i',[])
n=int(input("Enter the Number of Elements: "))
for i in range(n):
      x=int(input('Enter Element Numbers[{}]: '.format(i)))
      num.append(x)
print('The Array Elements are:- ')
for i in num:
    print(i,'\t',end='')
