#Prog03B3: Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input 
# when the inputted number have duplicate.
#continue asking until the user input is invalid.
#Display "Unique" after input when the inputted number don't have duplicate.
#Display "Duplicate" after input when the inputted number have duplicate.
# Program to handle number input and check for duplicates

all_numbers = []  
unique_numbers = []  

while True:
    try:
        # Input a number
        number = int(input("Enter a number (Enter an invalid input to stop): "))

        # Store the number in all_numbers (even duplicates)
        all_numbers.append(number)

        # Check if the number is unique (to maintain order)
        if number in unique_numbers:
            print("Duplicate Number")
        else:
            print("Unique Number")
            unique_numbers.append(number)  # Add only first occurrences

    except ValueError:
        print("\nInvalid input - stopping program.")
        break  # Stop taking input when an invalid entry is made

# Display all numbers entered (including duplicates)
print("\nAll numbers entered:")
for num in all_numbers:
    print(num)  # Print each number on a new line

# Display only the first occurrence of each number
print("\nNumbers (showing only first occurrence):")
for num in unique_numbers:
    print(num)