#Prog01B3: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
#input ten numbers 
#create if statement to only display numbers without duplicates
#display all numbers that don't have duplicate

numbers = 0

for i in range(10):
    numbers = int(input(f"Enter the number {i+1}:"))
    if numbers not in (numbers_list + [None]):
        print(numbers)