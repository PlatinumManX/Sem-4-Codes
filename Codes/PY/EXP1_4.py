for i in range(1,1000,1):
    j=i
    num=i
    count=0
    sum=0
    while i!=0:
        count=count+1
        i=i//10
    while num!=0:
        rem=num%10
        sum=sum+(rem**count)
        num=num//10
    if sum==j:
        print("%d"%sum)
        
