#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
#input base number and exponent number
#multiply 
#print the result

# get user input for base number and exponent number
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))

# calculate the result by raising base to exponent
result = base ** exponent

# print the result
print(f"The result of {base} raised to the power of {exponent} is: {result}")