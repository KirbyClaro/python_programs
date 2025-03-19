#Prog02B5: Create a program that ask the user to input a number (0-1000). 
# Print the number in 6 digit format. Add zeros at the 
# beginning to complete the 6 digit.

    number_input = int(input("Enter a number (0-1000): "))
    formatted_number = str(number_input).zfill(6)

    print("The number in 6 digit format is:", formatted_number)
