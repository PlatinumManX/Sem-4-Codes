string=input("Enter a String: ")
count=0
vowels= "aeiouAEIOU"
for i in string:
    for j in vowels:
        if j==i:
            count=count+1
print("Number of Vowels in the String is: {}".format(count)) 
