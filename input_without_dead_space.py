#Prog01B5: Create a program that ask the user to input their 
#fullname with several space characters at the beginning. 
#Print the input without the spaces in the beginning.

user_input_name = input("Enter your name: ")

removed_space = user_input_name.lstrip()

print("Output:", removed_space)