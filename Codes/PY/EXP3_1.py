def pangram(string):
    "Function to check Whether the String is Pangram or not"
    low=string.lower()
    flag=0
    words="abcdefghijklmnopqrstuvwxyz"
    for i in words[::1]:
        if i in low:
            continue
        else:
            flag=1
    if flag==0:
        print("The String is Pangram")
    else:
        print("The String is not Pangram")

string=input("Enter a String to Check: ")
pangram(string)
