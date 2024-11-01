# Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

# Taking user input
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower() # Strip removes any whitespace and lower makes the check case insensitive

# String check
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
