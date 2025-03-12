#Prog03B3: Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input 
# when the inputted number have duplicate.
#continue asking until the user input is invalid.
#Display "Unique" after input when the inputted number don't have duplicate.
#Display "Duplicate" after input when the inputted number have duplicate.

numbers = []

#get user input for 10 numbers and store them in the list 'numbers'
print("Enter 10 Numbers")
for i in range(20):
    numbers_input = int(input(f"Enter the number {i+1}: "))
    numbers.append(numbers_input)

#find and display unique numbers
unique_numbers = [numbers_input for numbers_input in numbers if numbers.count(numbers_input) == 1]
print("Unique numbers:", unique_numbers)