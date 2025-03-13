#Prog03B4: Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the highest number
#input number till user input is invalid
#find the highest number
#display the highest number

# Initialize an empty list to store the numbers.
numbers = []

# Ask user to input numbers until user input is invalid.
while True:
    try:
        number_input = int(input("Enter a number (press Enter to stop): "))
        numbers.append(number_input)
    except ValueError:
        break