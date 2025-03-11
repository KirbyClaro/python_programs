#Prog10B2: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
#input two numbers
#use range to determine the numbers in between 
#print the numbers between two numbers

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print(f"The numbers between {first_number} and {second_number} are:")
for i in range(min(first_number, second_number), max(first_number, second_number)) :
    print(i)