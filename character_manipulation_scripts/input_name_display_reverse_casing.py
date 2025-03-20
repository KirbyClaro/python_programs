#Prog06B5: Create a program that ask the user to input 
# their fullname in incorrect casing. Print 
# each character of the input in reverse casing.

#input the user's name
fullname = input("Enter your fullname: ")

#reverse casing each character of the input name 
for letter in fullname:
    if letter.isupper():
        reverse_casing += letter.lower()
    elif letter.islower():
        reverse_casing += letter.upper()
    else:
        reverse_casing += letter

#print the reverse casing 
print("Reverse casing of your fullname:", reverse_casing)