print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q21
print("Q21-Write a python program that counts the occurrences of a specific element in a list:",end="\n\n")
L=[1,2,3,4,5,6,4,3,2,6,7,5,4,32,2,'a','b','c',1.3,2.4]
print("List given-",L)
l=[]
for i in L:
    l.append(str(i))
x=input("Enter the specific element-")
print("Count of",x,"is:",l.count(x),end="\n\n")
