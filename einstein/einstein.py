# Implement a program in Python that prompts the user for mass as an integer (in kilograms)
# and then outputs the equivalent number of Joules as an integer.
# Assume that the user will input an integer.

# Defining variables
mass = int(input("m: ")) # Mass has to be an integer
speed = 300000000

# Calculating energy
energy = mass * pow(speed, 2)
print("e:", energy)
