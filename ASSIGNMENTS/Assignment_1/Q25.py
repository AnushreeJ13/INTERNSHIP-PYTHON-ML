print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q25
print("Q25-Write a program that copies the contents of one text file to another:",end="\n\n")
s1=open(r"C:\Users\Anushree Jain\OneDrive\Desktop\COLLEGE\INTERNSHIP\ASSIGNMENTS\Assignment_1\demo.txt",'r')
content=s1.read()
s1.close()
s2=open(R"C:\Users\Anushree Jain\OneDrive\Desktop\COLLEGE\INTERNSHIP\ASSIGNMENTS\Assignment_1\demo2.txt",'w')
print(content,file=s2)
print("Content copied in demo2 from demo!!!",end="\n\n")
s2.close()
