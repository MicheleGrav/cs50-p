# Implement a program in Python that prompts the user for input and then outputs that same input,
# replacing each space with ... (i.e., three periods).

# Taking user input
text = input()

# Replacing the spaces with three periods using .replace() string method
new_text = text.replace(' ', '...')
print(new_text)
