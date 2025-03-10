#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
#input two numbers with decimal point
#divide the numbers
#print result of the program

#input the numerator and denominator
numerator  = float(input("Enter the first number (Numerator): "))
denominator = float(input("Enter the second number (Denominator): "))

#calculate the quotient
qoutient = numerator / denominator

#print the quotient with decimal point
print("The quotient of", numerator, "and", denominator, "is", qoutient)