#Prog05B2: Create a program that ask user to input 2 numbers. Print the remainder 
# when the first number is divided by the second number.
#input two numhbers 
#divide the numbers and print the remainder 
#print the remainder

#input two numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: ")) 

#divide the numbers and print the remainder
remainder = first_number % second_number

#print the remainder
print("The remainder when", first_number, "is divided by", second_number, "is:", remainder)