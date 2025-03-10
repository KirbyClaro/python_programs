#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
#use a for statement
#if else statements for picking only the even numbers
#print the even numbers

#use range to determine the number of numbers 
for i in range(101):
    #check if the number is even by checking if it's divisible by 2 without leaving a remainder
    if i % 2 == 0:
        #if the number is even, print it
        print(i)