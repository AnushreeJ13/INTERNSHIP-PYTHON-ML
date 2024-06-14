print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q15
print("Q15-Write a program that reads data from a CSV file(C1) and prints it to the console:",end="\n\n")
import  pandas as pd
data=pd.read_csv(r"C:\Users\Anushree Jain\OneDrive\Desktop\COLLEGE\INTERNSHIP\ASSIGNMENTS\Assignment_1\C1.csv")
print("Contents of csv:",data,sep="\n",end="\n\n")
