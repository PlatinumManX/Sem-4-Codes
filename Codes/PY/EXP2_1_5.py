import array
num1 = array.array('i',[])
n1=int(input("Enter the Number of Elements in Array 1: "))
for i in range(n1):
      x=int(input('Enter Element Numbers[{}]: '.format(i)))
      num1.append(x)
import array
num2 = array.array('i',[])
n2=int(input("Enter the Number of Elements in Array 2: "))
for i in range(n2):
      x=int(input('Enter Element Numbers[{}]: '.format(i)))
      num2.append(x)
num1.extend(num2)
print("Array After Extending is:- ",end='')
for i in num1:
        print(i,'\t',end='')
