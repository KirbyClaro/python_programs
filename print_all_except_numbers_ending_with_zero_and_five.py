#Prog09B2: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five
#use while statement to print only the numbers starting from 0 to 100
#create if statement to not print the numbers ending in zero or ending five
#print the numbers

#initialize 
i = 0

#use while loop to print numbers from 0 to 100
while i <= 100:
    #check if the number is not ending in zero or five and print it 
    if i % 10 != 0 and i % 10 != 5:
        print(i)
    #increment the counter
    i += 1