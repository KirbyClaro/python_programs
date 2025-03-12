#Prog04B3: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
#ask user to input till invalid
#only display the lowest number

while True:
    try:
        # Input a number
        number = int(input("Enter a number (Enter an invalid input to stop): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    break

lowest_number = min(number)