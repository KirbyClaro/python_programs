#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
#input ten numbers using range 
#add the even numbers to the count
#print all the even numbers counted

even_numbers_count = 0

for i in range(10):
    numbers = int(input(f"Enter the number {i+1}: "))
    if numbers % 2 == 0:
        even_numbers_count += 1

print(f"The count of even numbers is: {even_numbers_count}")