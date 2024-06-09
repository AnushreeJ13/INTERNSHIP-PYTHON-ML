print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q1
print("Q1-Write a program that takes two numbers as input and prints their sum:")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The sum of numbers is:",a+b,sep="",end="\n\n")

# Q2
print("Q2-Write a python program that checks whether a given number is even or odd:")
a=int(input("Enter a number:"))
if a%2==0:
    print("Number is even",end="\n\n")
else:
    print("Number is odd",end="\n\n")

# Q3
print("Q3-Write a python program that calculates the factorial of a given number:")
import  math as mt
a=int(input("Enter a number:"))
print("Factorial of given number is:",mt.factorial(a),end="\n\n")

# Q4
print("Q4-Write a program that asks the user for their name and then prints a greeting message:")
x=input("Enter your name-")
print("Hello",x)
print("Welcome to Github!",end="\n\n")

# Q5
print("Q5-Write a program that takes a string input from the user and writes it to a text file:")
x=input("Enter any message-")
samplefile=open(R"C:\Users\Anushree Jain\OneDrive\Desktop\COLLEGE\INTERNSHIP\demo.txt",'w')
print("Message has been stored in file demo.",end="\n\n")
print(x,file=samplefile)
samplefile.close()

# Q6
print("Q6-Write a program that reads the content of a text file and prints it to the console:")
samplefile1=open("C:/Users/Anushree Jain/OneDrive/Desktop/COLLEGE/INTERNSHIP/demo.txt",'r')
print("Message stored in demo file is-",samplefile1.read(),end="\n")
samplefile1.close()

# Q7
print("Q7-Write a python program that takes a string as input and returns its length:")
x=input("Enter a string-")
print("Length of string is:",len(x),end="\n\n")

# Q8
print("Q8-Write a python program that concatenates two strings and returns the result:")
x=input("Enter first string-")
y=input("Enter second string-")
result=x+y
print(result,end="\n\n")

# Q9
print("Q9-Write a python program that checks if a substring is present in a given string:")
s="A warm welcome to all my visitors"
x=input("Enter a substring-")
print(x,"(substring) is present in the string-",x in s)
print("String is-",s,end="\n\n")
# Q10
print("Q10-Write a python program that converts a given string to uppercase:")
x=input("Enter a string-")
print(x,"(UPPER)-",x.upper(),end="\n\n")

# Q11
print("Q11-Write a python program that generates the first n numbers in the Fibonacci sequence:")
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

# Q12
print("Q12-Write a python program that calculates the sum of the digits of a given number:")
a=input("Enter a number:")
sum=0
for i in a:
    sum+=int(i)
print("Sum of digits of",int(a),"is:",sum,end="\n\n")

# Q13
print("Q13-Write a program that asks the user for their birth year and calculates their age:")
import datetime as dt
sys=dt.datetime.now()
date=sys.date()
current_year=date.strftime("%Y")
a=int(input("Enter your birth year:"))
age=int(current_year)-a
print("Your age is:",age,end="\n\n")

# Q14
print("Q14-Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines:")
print("Enter your text-")
user_input = ""
while True:
    line = input()
    if line=="":
        break
    user_input += line + "\n"

print("You entered:\n" + user_input)

# Q15
print("Q15-Write a program that reads data from a CSV file(C1) and prints it to the console:")
import  pandas as pd
data=pd.read_csv(r"C:\Users\Anushree Jain\OneDrive\Desktop\COLLEGE\INTERNSHIP\C1.csv")
print("Contents of csv:",data,end="\n\n")

# Q16
print("Q16-Write a program in python that counts the frequency of each character ina string:")
x=input("Enter a string-")
y=""
for i in x:
    if y.find(i)==-1:
        print(i,"-",x.count(i))
        y+=i

# Q17
print("Q17-Write a program in python that converts a given string to title case (firstletter of each word capitalized):")
x=input("Enter a string-")
print(x,"(title case)-",x.title(),end="\n\n")

# Q18
print("Q18-Write a python program that checks if two strings are anagrams of each other:")
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

# Q19
print("Q19-Write a python program that removes all punctuation from a given string:")
import string
x=input("Enter the string-")
for i in x:
    if i in string.punctuation:
        x=x.replace(i,"")
print(x,end="\n\n")  

# Q20
print("Q20-Write a python program that takes a list of numbers and returns their sum:")
n=int(input("Enter the number of elements:"))
l=[]
for i in range(0,n):
    a=int(input("Enter the element:"))
    l.append(a)
sum=0
for j in l:
    sum+=j
print("Sum of elements is:",sum,end="\n\n")

# Q21
print("Q21-Write a python program that counts the occurrences of a specific element in a list:")
L=[1,2,3,4,5,6,4,3,2,6,7,5,4,32,2,'a','b','c',1.3,2.4]
print("List given-",L)
l=[]
for i in L:
    l.append(str(i))
x=input("Enter the specific element-")
print("Count of",x,"is:",l.count(x),end="\n\n")

# Q22
print("Q22-Write a python program that returns the minimum and maximum values in a list of numbers:")
l1=[2,3,4,56,7,5,33,5,8,5,-1]
print(l1)
print("Maximum number is:",max(l1))
print("Minimum number is:",min(l1),end="\n\n")

# Q23
print("Q23-Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input:")
a=input("Enter the temperature in Celsius:")
temp=(float(a)*9)/5+32
print(a,"in Fahrenheit:",temp)
b=input("Enter the temperature in Fahrenheit:")
temp=((float(b)-32)*5)/9
print(b,"in Celsius:",temp,end="\n\n")

# Q24
print("Q24-Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result:")
a=int(input("Enter the first number of calculator:"))
b=int(input("Enter the second number of calculator:"))
x=input("Enter the operator(+,-,*,/) for calculator-")
if x=="+":
    print("Sum of",a,"and",b,"is:",a+b,end="\n\n")
elif x=="-":
    print("Difference of",a,"and",b,"is:",a-b,end="\n\n")
elif x=="*":
    print("Multiplication of",a,"and",b,"is:",a*b,end="\n\n")
elif x=="/":
     print("Division of",a,"by",b,"is:",a/b,end="\n\n")

# Q25
print("Q25-Write a program that copies the contents of one text file to another:")
s1=open(r"C:\Users\Anushree Jain\OneDrive\Desktop\COLLEGE\INTERNSHIP\demo.txt",'r')
content=s1.read()
s1.close()
s2=open(R"C:\Users\Anushree Jain\OneDrive\Desktop\COLLEGE\INTERNSHIP\demo2.txt",'w')
print(content,file=s2)
print("Content copied in demo2 from demo!!!",end="\n\n")
s2.close()

# Q26
print("Q26-Write a program in python that checks if a string starts with a given prefix or ends with a given suffix:")
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

# Q27
print("Q27-Write a program in python that converts a string into a list of its characters:")
x=input("Enter a string-")
print("List of characters is-",list(x),end="\n\n\n")


print("THANK YOU FOR CHECKING MY ASSIGNMENT","HAVE A NICE DAY😊!",sep="\n",end="\n\n\n")