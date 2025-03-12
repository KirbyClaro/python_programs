#Prog03B3: Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input 
# when the inputted number have duplicate.
#continue asking until the user input is invalid.
#Display "Unique" after input when the inputted number don't have duplicate.
#Display "Duplicate" after input when the inputted number have duplicate.

# Program to handle number input and check for duplicates
numbers = []
while True:
    try:
        # Input a number
        number = int(input("Enter a number (Enter Invalid input to stop): "))
        
        # Check if number already exists in the list
        if number in numbers:
            print("Duplicate Number")
        else:
            print("Unique Number")
            numbers.append(number)

    except ValueError:
        print("\nInvalid input - stopping program.")
        break

    # Display all numbers entered
    print("\nAll numbers entered:")
    print(numbers)  # Print the entire list directly

    # Display the first occurrence of each number
    print("\nNumbers (showing only first occurrence):")
    for num in numbers:
        print(num)
