#Prog02B2: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
#input two numbers
#determine if two numbers are not equal
#print "Not Equal" if not equal

#input two numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

#determine if two numbers are not equal or equal
if first_number != second_number:
    print(f"{first_number} is not equal to {second_number}")
elif first_number == second_number:
    print(f"{first_number} is equal to {second_number}")