#Prog08B2: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
#use while loop with range to print all the numbers
#use if statement to check if numbers are odd
#print only the odd numbers starting from 0 to 100

i = 0

while i <= 100:
    if i % 2 != 0:
        print(i)
    i += 1