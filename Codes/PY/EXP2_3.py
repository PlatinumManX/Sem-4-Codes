string=input("Enter a String: ")
first=string[0]
l=len(string)
rep=input("Enter the character to Replace: ")
string=string.replace(first,rep)
string=first+string[1:]
print("String after Replacement is: ",string)
