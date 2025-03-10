#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
#input base number and exponent number
#multiply 
#print the result

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))

result = base ** exponent

print(f"The result of {base} raised to the power of {exponent} is: {result}")