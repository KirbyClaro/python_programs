#Prog07B5: Create a program that ask the user to input a 
#complete statement. Print the number of words in the input.

# Input a complete statement.
sentence = input("Enter a complete statement: ")

# Split the sentence into a list of words.
split_words = sentence.split()

# Calculate the number of words in the input statement.
word_count = len(split_words)

# Print the number of words in the input statement.
print(f"The number of words in the statement is {word_count}")