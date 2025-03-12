#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
#input 10 numbers
#add all the numbers
#print all the numbers

#set the value to 0
total_of_numbers = 0

#ask the user to input 10 numbers
print("Enter 10 numbers:")

#loop through the 10 numbers and add them to the total
for i in range(10):
    numbers = int(input(f"Enter number {i+1}: "))
    total_of_numbers += numbers

#print the sum of all the numbers
print("Sum of all numbers:", total_of_numbers)