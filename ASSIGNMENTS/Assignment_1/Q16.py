print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q16
print("Q16-Write a program in python that counts the frequency of each character in a string:",end="\n\n")
x=input("Enter a string-")
y=""
for i in x:
    if y.find(i)==-1:
        print(i,"-",x.count(i))
        y+=i
