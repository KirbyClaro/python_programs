#Prog04: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the number from highest to lowest. Clue: sort() function
#ask user to input numbers until user input is invalid
#sort numbers from highest to lowest
#print numbers

# Initialize an empty list to store the numbers.
numbers = []

# Ask user to input numbers until user input is invalid.
while True:
    try:
        number_input = int(input("Enter a number (press Enter to stop): "))
        numbers.append(number_input)
    except ValueError:
        break

# Sort the numbers from highest to lowest.
numbers.sort(reverse=True)

# Display the sorted numbers.
print("\nNumbers from highest to lowest:")
print(*numbers) if numbers else print("No valid numbers entered.")