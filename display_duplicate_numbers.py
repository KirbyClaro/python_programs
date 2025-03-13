#Prog01B4: Create a program that ask user to input 10 numbers. 
#Display all numbers that have duplicate.
#ask user to input 10 numbers
#seperate all numbers with duplicates

numbers = []

for i in range(10):
    numbers_input = int(input(f"Enter number {i+1}: "))
    numbers.append(numbers_input)

duplicates = {num for num in numbers if numbers.count(num) > 1}

print("Duplicate numbers:", duplicates)
