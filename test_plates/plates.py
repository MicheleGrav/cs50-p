# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters
# and numbers instead of random ones. Among the requirements, though, are:
#
# 1) “All vanity plates must start with at least two letters.”
# 2) “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# 3) “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# 4) “No periods, spaces, or punctuation marks are allowed.”
#
# Implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements
# or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
# Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
# Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if plate length is between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if the first two characters are letters
    if not s[0:2].isalpha():
        return False

    # Check if plate is alphanumeric (no periods, spaces, or punctuation)
    if not s.isalnum():
        return False

    has_num = False  # Flag to indicate if we've seen a number
    for c in s:
        # If a digit is found, ensure it is not the first number being 0 and that no letter follows after a number
        if c.isdigit():
            if c == '0' and not has_num:  # No leading zero in numbers
                return False
            has_num = True  # Mark that a number has been encountered
        elif has_num and c.isalpha():  # If a letter comes after a number, return False
            return False

    # All checks passed, return True
    return True

if __name__ == "__main__":
    main()
