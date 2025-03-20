#Prog06B5: Create a program that ask the user to input 
# their fullname in incorrect casing. Print 
# each character of the input in reverse casing.

fullname = input("Enter your fullname: ")

reverse_casing = ""
for letter in fullname:
    if letter.isupper():
        reverse_casing += letter.lower()
    elif letter.islower():
        reverse_casing += letter.upper()