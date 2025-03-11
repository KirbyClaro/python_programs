#Prog09B2: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five
#use while statement to print only the numbers starting from 0 to 100
#create if statement to not print the numbers ending in zero or ending five
#print the numbers

i = 0

while i <= 100:
    if i % 10 != 0 and i % 10 != 5:
        print(i)
    i += 1