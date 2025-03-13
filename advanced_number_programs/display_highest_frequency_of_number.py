#Prog02B4: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the number with the most number of duplicate.
#ask user to input numbers until user input is invalid
#count occurance of numbers
#display number with the most number of duplicate

# Initialize an empty list to store the numbers.
numbers = []

# Ask user to input numbers until user input is invalid.
while True:
    try:
        number_input = int(input("Enter a number (press Enter to stop): "))
        numbers.append(number_input)
    except ValueError:
        break

# If there are any numbers in the list, calculate the most frequent number.
if numbers:
    count_dictionary = {number_input: numbers.count(number_input) 
                        for number_input in set(numbers)}

    most_frequent = max(count_dictionary, key=count_dictionary.get)

    # Display the number with the most number of duplicate.
    print(f"The number with the most number of duplicate is: {most_frequent}")
else:
    # Display a message if no numbers were entered.
    print("No numbers entered.")