#Prog02B5: Create a program that ask the user to input a number (0-1000). 
# Print the number in 6 digit format. Add zeros at the 
# beginning to complete the 6 digit.
try:
    number_input = int(input("Enter a number (0-1000): "))

    if 0 =< number_input =< 1000:
        formatted_number = str(number_input).zfill(6)
        print("The number in 6 digit format is:", formatted_number)
    else
        print("Invalid input. Please enter a number between 0 and 1000.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
    
