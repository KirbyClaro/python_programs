#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
#input two numbers with decimal point
#divide the numbers
#print result of the program

numerator  = int(input("Enter the first number (Numerator): "))
denominator = int(input("Enter the second number (Denominator): "))

qoutient = numerator // denominator

print("The quotient of", numerator, "and", denominator, "is", qoutient)