print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q26
print("Q26-Write a program in python that checks if a string starts with a given prefix or ends with a given suffix:",end="\n\n")
s="WHOAAAAAAA!!!"
x=input("Given prefix-")
if s[0:len(x)]==x:
    print("Yes it starts with given prefix")
else:
    print("No it doesn't start with given prefix")
y=input("Given suffix-")
if s[len(s)-len(y):]==y:
    print("Yes it ends with given prefix")
else:
    print("No it doesn't end with given suffix")
print("The string is-",s,end="\n\n")
