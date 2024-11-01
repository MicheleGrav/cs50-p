# Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
# For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.
#
# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
# and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.
#
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.)
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    fraction = get_fraction("Fraction: ") # Passing prompt to get_fraction()
    percent = convert_perc(fraction)
    # Cases where tank is empty or full
    if percent <= 1:
        print('E')
    elif percent >= 99:
        print('F')
    else:
        print(f"{percent}%") # Otherwise print the percentage value

# Function that manages input
def get_fraction(prompt):
    while True:
        try:
            frac = input(prompt) # Get input (returns string)
            x, y = frac.split('/') # Assign x and y from input string

            # Casting to integer
            x = int(x)
            y = int(y)

            # Raising errors according to exercise request
            if x > y:
                raise ValueError
            if y == 0:
                raise ZeroDivisionError

            return (x, y) # Return x and y as tuple
        except (ValueError, ZeroDivisionError) as e:
            pass # We don't want to print anything for the errors raised

# Function that converts the input fraction into its respective percentage value
def convert_perc(fraction):
    x, y = fraction # Assign the tuple values respectively to x and y
    return round((x / y) * 100)

main()
