# Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a
# floating-point value formatted to one decimal place.
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

# Take user input
expr = input("Expression: ")

x, y, z = expr.split(" ")

# Casting string to integer
xint = int(x)
zint = int(z)

# Checking operations
match y:
    case '+':
        res = xint + zint
    case '-':
        res = xint - zint
    case '/':
        res = xint / zint
    case '*':
        res = xint * zint
    case _:
        print("Operation not valid.")

print(f"{res:.1f}")
