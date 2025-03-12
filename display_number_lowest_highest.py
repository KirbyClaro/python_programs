#Prog05B3: Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display the number from lowest to highest. Clue: sort() function
#ask user to input till user input is invalid 
#sort values inputed by user input from lowest to highest
#display the number from lowest to highest

numbers = []
    
while True:
    try:
        # Get user input
        num_input = input("Enter a number (press Enter to stop): ")
        
        # Check if user wants to stop
        if num_input.strip() == "":
            break
                
        # Convert input to float and add to list
        number = float(num_input)
        numbers.append(number)
            
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    # Display sorted numbers if any
    if len(numbers) == 0:
        print("No numbers were entered.")
    else:
        # Sort numbers from lowest to highest
        sorted_numbers = sorted(numbers)
        print("\nNumbers in order from lowest to highest:")
        for num in sorted_numbers:
            print(num)