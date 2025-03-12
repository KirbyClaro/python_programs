#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
#input ten numbers
#add count to odd_numbers_count if number is odd
#print odd_numbers_count

#initialize count of odd numbers
odd_numbers_count = 0

#prompt user to enter 10 numbers and count odd numbers
for i in range(10):
    numbers = int(input(f"Enter numbers {i+1}: "))
    
    #check if number is odd and increment count if it is
    if numbers % 2 != 0:
        odd_numbers_count += 1

#print the count of odd numbers entered
print(f"The number of odd numbers entered is: {odd_numbers_count}")