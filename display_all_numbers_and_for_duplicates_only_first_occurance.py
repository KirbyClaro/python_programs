#Prog02B3: Create a program that ask user to input 10 numbers. 
# Display all numbers. For numbers with duplicate, display only the first entry.
#input ten numbers
#create list for the numbers
#print all numbers
#find and display first occurrence of each number

print("Enter 10 numbers:")
for i in range(10):
    numbers = float(input(f"Enter each number {i+1}: "))