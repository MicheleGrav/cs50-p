# Implement a Python function called convert which turns all :( and :) in 🙁 and 🙂 respectively

# Defining the convert function
def convert(text):
    return text.replace(":(", "🙁").replace(":)", "🙂") # The function uses the string .replace() method

# Taking user input
txt = input()

# Calling convert function and printing
print(convert(txt))
