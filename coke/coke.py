# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
# 25 cents, 10 cents, and 5 cents.
#
# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time,
# each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def main():
    num = get_coin()
    print(f"Change Owed: {abs(num)}") # Absolute value of the change which is negative or zero

def get_coin():
    s = 50
    while s > 0:
        print(f"Amount Due: {s}")
        coin = int(input("Insert Coin: ")) # Cast to integer
        if not validate(coin):
            continue
        else:
            s -= coin # Subtract the added amount from total
    return s

# Function that validates the coin input
def validate(coin):
    return coin in [25, 10, 5]

main()
