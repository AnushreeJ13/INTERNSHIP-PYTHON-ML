print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q24
print("Q24-Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result:",end="\n\n")
a=input("Enter the first number of calculator:")
b=input("Enter the second number of calculator:")
x=input("Enter the operator(+,-,*,/) for calculator-")
if x=="+":
    print("Sum of",a,"and",b,"is:",float(a)+float(b),end="\n\n")
elif x=="-":
    print("Difference of",a,"and",b,"is:",float(a)-float(b),end="\n\n")
elif x=="*":
    print("Multiplication of",a,"and",b,"is:",float(a)*float(b),end="\n\n")
elif x=="/":
     print("Division of",a,"by",b,"is:",float(a)/float(b),end="\n\n")
