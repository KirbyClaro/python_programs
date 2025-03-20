#Prog09B5: Create a program that ask the user 
#to input their fullname in incorrect casing. 
# Print the input in pascal case.

fullname = input("Please enter your fullname: ")

split_fullname = fullname.split()

pascal_case = ""
for word in split_fullname:
    pascal_case += word[0].upper()
    pascal_case += word[1:].lower()

print("Pascal Case:", pascal_case)