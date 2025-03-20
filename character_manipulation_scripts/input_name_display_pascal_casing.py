#Prog09B5: Create a program that ask the user 
#to input their fullname in incorrect casing. 
# Print the input in pascal case.

#input the user's name in incorrect casing
fullname = input("Please enter your fullname: ")

#convert the input name to pascal case
split_fullname = fullname.split()

#concatenate the words in pascal case, capitalizing the first letter of each word
pascal_case = ""
for word in split_fullname:
    pascal_case += word[0].upper()
    pascal_case += word[1:].lower()

#print the input in pascal case
print("Pascal Case:", pascal_case)