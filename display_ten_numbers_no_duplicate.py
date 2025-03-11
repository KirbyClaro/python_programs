#Prog01B3: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
#input ten numbers 
#create if statement to only display numbers without duplicates
#display all numbers that don't have duplicate

numbers = 0

print("Enter 10 Numbers")
for i in range(10):
    numbers_input = int(input(f"Enter the number {i+1}:"))
    numbers.append(numbers_input)

unique_numbers = [numbers_input for numbers_input in numbers if numbers.count(numbers_input) == 1]
print("Unique numbers:", unique_numbers)