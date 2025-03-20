#Prog10: Create a program that ask the user 
# to input their fullname in incorrect casing. 
# Print the input in snake case.

#input the user's name in incorrect casing
fullname = input("Please enter your fullname: ")

#convert the input name to pascal case
split_fullname = fullname.split()

#convert the first letter of each word to lowercase and join them with underscores
snake_case = "_".join(split_fullname.lower() for split_fullname in split_fullname)

#print the input name in snake case
print("Output:", snake_case)