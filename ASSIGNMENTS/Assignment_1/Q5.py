print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q5
print("Q5-Write a program that takes a string input from the user and writes it to a text file:",end="\n\n")
x=input("Enter any message-")
samplefile=open(R"C:\Users\Anushree Jain\OneDrive\Desktop\COLLEGE\INTERNSHIP\ASSIGNMENTS\Assignment_1\demo.txt",'w')
print("Message has been stored in file demo.",end="\n\n")
print(x,file=samplefile)
samplefile.close()
