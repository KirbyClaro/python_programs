#Prog07B2: Create a program that ask user to input 10 numbers. Print how many are even numbers.
#input ten numbers using range 
#add the even numbers to the count
#print all the even numbers counted

#initialize count of even numbers
even_numbers_count = 0

#prompt user to enter 10 numbers and count even numbers
for i in range(10):
    numbers = int(input(f"Enter the number {i+1}: "))
    #check if number is even and increment count if it is
    if numbers % 2 == 0:
        even_numbers_count += 1

#print the count of even numbers entered
print(f"The count of even numbers is: {even_numbers_count}")