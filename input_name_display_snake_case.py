#Prog10: Create a program that ask the user 
# to input their fullname in incorrect casing. 
# Print the input in snake case.

#input the user's name in incorrect casing
fullname = input("Please enter your fullname: ")

#convert the input name to pascal case
split_fullname = fullname.split()

snake_case = "_".join(split_fullname.lower() for split_fullname in split_fullname)

print("Output:", snake_case)