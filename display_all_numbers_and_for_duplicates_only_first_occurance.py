#Prog02B3: Create a program that ask user to input 10 numbers. 
# Display all numbers. For numbers with duplicate, display only the first entry.
#input ten numbers
#create list for the numbers
#print all numbers
#find and display first occurrence of each number

numbers = []

print("Enter 10 numbers:")
for i in range(10):
    numbers_ten = int(input(f"Enter number {i+1}: "))
    numbers.append(numbers_ten)

print("\nAll numbers entered:")
for number in numbers:
    print(number)

print("\nNumbers (showing only first occurrence):")
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        print(number)
        unique_numbers.append(number)