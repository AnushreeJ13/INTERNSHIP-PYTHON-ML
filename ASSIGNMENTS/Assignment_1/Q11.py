print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q11
print("Q11-Write a python program that generates the first n numbers in the Fibonacci sequence:",end="\n\n")
a=0
b=1
n=int(input("Enter a number(FIBONACCI SERIES):"))
if n==0:
    print("")
else:
    if n==1:
        print(a)
    else:
        if n==2:
            print(a,b)
        else:
            if n>2:
                print(a,b,end=" ")
                for i in range(3,n+1):
                    c=a+b
                    a=b
                    b=c
                    print(c,end=" ")
print("",end="\n\n")
