print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q18
print("Q18-Write a python program that checks if two strings are anagrams of each other:",end="\n\n")
x=input("Enter the first string-")
y=input("Enter the second string-")
c=0
if len(x)==len(y):
    for i in x:
        if y.find(i)==-1:
            break
        else:
            c+=1
    if c==len(x):
        for i in y:
            if x.find(i)==-1:
                break
            else:
                c+=1
    if c==2*len(y):
        print("Yes the strings are anagrams of each other",end="\n\n")
    else:
        print("No the strings are not anagrams of each other",end="\n\n")
            
else:
    print("No the strings are not angrams of each other",end="\n\n")
