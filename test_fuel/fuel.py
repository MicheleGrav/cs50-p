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
    fraction = get_fraction("Fraction: ")  # Prompt for user input
    percent = convert(fraction)  # Convert the fraction to a percentage
    result = gauge(percent)  # Get the gauge output based on the percentage
    print(result)  # Print the result


def convert(fraction):
    try:
        x, y = fraction.split('/')  # Split the input string
        x = int(x)  # Convert X to an integer
        y = int(y)  # Convert Y to an integer

        # Raise exceptions based on the problem's requirements
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError

        # Calculate and return the percentage, rounded to the nearest integer
        percentage = round((x / y) * 100)
        return percentage
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    if percentage <= 1:
        return "E"  # Empty tank indicator
    elif percentage >= 99:
        return "F"  # Full tank indicator
    else:
        return f"{percentage}%"  # Return the percentage as a string


def get_fraction(prompt):
    while True:
        try:
            frac = input(prompt)  # Get input from the user
            return frac
        except Exception:
            pass


if __name__ == "__main__":
    main()
