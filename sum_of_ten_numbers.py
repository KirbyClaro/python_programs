#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
#input 10 numbers
#add all the numbers
#print all the numbers

total_of_numbers = 0
print("Enter 10 numbers:")

for i in range(10):
    numbers = int(input(f"Enter number {i+1}: "))
    total_of_numbers += numbers

print("Sum of all numbers:", total_of_numbers)