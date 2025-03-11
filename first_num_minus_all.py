#Prog06B2: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
#input first number
#add range for nine remaining numbers and add all of the remaining numbers
#minus first number to the remaining numbers
#print the result of the first number minus all of the remaining numbers

#input first number
first_number = int(input("Enter the first number: "))

result = first_number 

#add range for nine remaining numbers and add all of the remaining numbers
for i in range(9):
    numbers = int(input(f"Enter the number {i+1}:"))
    #formula for the first number minus all of the remaining numbers
    result -= numbers

#print the result of the first number minus all of the remaining numbers
print("The result of", first_number, "minus all of the remaining numbers is:", result)