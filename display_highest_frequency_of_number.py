#Prog02B4: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the number with the most number of duplicate.
#ask user to input numbers until user input is invalid
#count occurance of numbers
#display number with the most number of duplicate

numbers = []

while true:
    try:
        number_input = int(input("Enter a number (press Enter to stop): "))
        numbers.append(number_input)
    except ValueError:
        break

if numbers:
    count_dictionary = {number_input: numbers.count(number_input) for number_input in set(numbers)}

    most_frequent = max(count_dictionary, key=count_dictionary.get)

    print(f"The number with the most number of duplicate is: {most_frequent}")
else:
    prindt("No numbers entered.")