#Prog04B3: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
#ask user to input till invalid
#only display the lowest number

lowest_number = float('inf')

while True:
    try:
        # Input a number
        number_input = input("Enter a number (Enter an invalid input to stop): ")

        if number_input.strip() == "":
            break

        number = float(number_input)

        lowest_number = min(lowest_number, number)

    except ValueError:
        print("Invalid input. Program will now exit.")
        break

if lowest_number == float('inf'):
    print("No numbers were entered.")
else:
    print(f"The lowest number entered was: {lowest_number}")

