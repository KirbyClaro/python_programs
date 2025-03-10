#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
#input ten numbers
#add count to odd_numbers_count if number is odd
#print odd_numbers_count

odd_numbers_count = 0

for i in range(10):
    numbers = int(input(f"Enter numbers {i+1}: "))
    if numbers % 2 != 0:
        odd_numbers_count += 1

print(f"The number of odd numbers entered is: {odd_numbers_count}")