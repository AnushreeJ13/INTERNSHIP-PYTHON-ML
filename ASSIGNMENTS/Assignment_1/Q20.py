print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q20
print("Q20-Write a python program that takes a list of numbers and returns their sum:",end="\n\n")
n=int(input("Enter the number of elements:"))
l=[]
for i in range(0,n):
    a=int(input("Enter the element:"))
    l.append(a)
sum=0
for j in l:
    sum+=j
print("Sum of elements is:",sum,end="\n\n")
