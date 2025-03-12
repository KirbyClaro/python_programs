#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
#use a for statement
#if else statements for picking only the numbers ending in zero
#print the numbers not ending in zero

#use range to determine the number of numbers
for i in range(101):
    #check if the last digit is not zero
    if i % 10!= 0:
        #print the number if it meets the condition
        print(i)
