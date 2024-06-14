print("                                                         ASSIGNMENT-1[ANUSHREE JAIN]",end="\n\n")


# Q14
print("Q14-Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines:",end="\n\n")
print("Enter your text-")
user_input = ""
while True:
    line = input()
    if line=="":
        break
    user_input += line + "\n"

print("You entered:\n" + user_input)
