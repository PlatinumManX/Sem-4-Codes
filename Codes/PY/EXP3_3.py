def decor1(func):
    def inner(n):
        value=func(n)
        return value+4
    return inner
def decor2(func):
    def inner(n):
        value=func(n)
        return value*2
    return inner
def square(n):
    return n*n
def cube(n):
    return n*n*n
num=int(input("Enter a Number: "))
res1=decor1(square)(num)
res2=decor2(cube)(num)
print("The Square of the Number is: ",res1)
print("The Cube of the Number is: ",res2)
