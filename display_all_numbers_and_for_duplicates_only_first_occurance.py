#Prog02B3: Create a program that ask user to input 10 numbers. 
# Display all numbers. For numbers with duplicate, display only the first entry.
#input ten numbers
#create list for the numbers
#print all numbers
#find and display first occurrence of each number
numbers = []

print("Enter 10 numbers:")
for i in range(10):
    numbers_ten = int(input(f"Enter each number {i+1}: "))
    

print("all numbers entered:")
for numbers_ten in numbers:
    print(numbers)

print("\nNumbers (showing only first occurrence):")
unique_numbers = [] 
for numbers_ten in numbers:
    if numbers_ten not in unique_numbers:
        print(numbers_ten)
        unique_numbers.append(numbers_ten)