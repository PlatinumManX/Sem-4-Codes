def summation(numbers):
    return sum(numbers)
def product(numbers):
    result=1
    for i in numbers:
        result=result*i
    return result
def sumeven(numbers):
    j=1
    evensum=0
    for i in numbers:
        if j%2==0:
            evensum=evensum+i
        j=j+1
    return evensum
def app(numbers, num):
    numbers.append(num)
    return numbers
