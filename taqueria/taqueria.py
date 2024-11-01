# In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program).
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
# Treat the user’s input case insensitively.
# Ignore any input that isn’t an item.
# Assume that every item on the menu will be titlecased.

def main():
    s = 0 # Total cost
    while True:
        try:
            item = input("Item: ").strip().lower() # Remove extra whitespaces and setting everything to lowercase to fix capitalization typos
            price = check_price(item)
            if price is not None:
                s += price
                print(f"Total: ${s:.2f}") # Formatted to two decimal places
        except EOFError: # Managing CTRL + D
            print("") # Print already adds a \n by default, no need to add \n between quotation marks
            break

# Function that checks the price of the items using a dictionary
def check_price(item):
    items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    return items.get(item.title(), None) # .get() function takes the item name titlecased and returns None if no valid key is found


main()
