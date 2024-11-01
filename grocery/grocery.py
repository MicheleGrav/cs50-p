# In a file called grocery.py, implement a program that prompts the user for items, one per line, until
# the user inputs control-d (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
# No need to pluralize the items. Treat the user’s input case-insensitively.

def main():
    grocery = {} # Empty dictionary
    while True:
        try:
            item = input().upper() # Turning input to uppercase
            if item in grocery:
                grocery[item] += 1  # Increment count if item was already inserted
            else:
                grocery[item] = 1 # First time adding item, set count to one
        except EOFError:
            print('') # Going newline after CTRL + D
            break
    for item, amount in sorted(grocery.items()): # Sorting dict alphabetically and iterating, saving values in 'item' and 'amount'
        print(f"{amount} {item}")

main()
