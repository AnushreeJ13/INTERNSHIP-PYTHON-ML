print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q19
print("Q19-Write a python program that removes all punctuation from a given string:",end="\n\n")
import string
x=input("Enter the string-")
for i in x:
    if i in string.punctuation:
        x=x.replace(i,"")
print(x,end="\n\n")  
