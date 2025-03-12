#Prog08B2: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
#use while loop with range to print all the numbers
#use if statement to check if numbers are odd
#print only the odd numbers starting from 0 to 100

#initialize counter variable i to 0
i = 0

#use while loop to iterate until i is less than or equal to 100
while i <= 100:
    #check if the number is odd by checking if it's divisible by 2 without leaving a remainder
    if i % 2 != 0:
        print(i)
    #increment i by 1 to move to the next number in the loop
    i += 1