print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q13
print("Q13-Write a program that asks the user for their birth year and calculates their age:",end="\n\n")
import datetime as dt
sys=dt.datetime.now()
date=sys.date()
current_year=date.strftime("%Y")
a=int(input("Enter your birth year:"))
age=int(current_year)-a
print("Your age is:",age,end="\n\n")
