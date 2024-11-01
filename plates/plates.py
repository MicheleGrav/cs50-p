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
    return check1(s[0:2]) and check2(s) and check3(s) and check4(s)

def check1(s):
    return s.isalpha() # Passing substring of first two characters and checking if they're letters

def check2(s):
    return (2 <= len(s) <= 6) # Checking length boundaries for the whole string

def check3(s):
    has_num = False # Bool variable to check if we encounter numbers
    for c in s:
        if c.isdigit():
            if c == '0' and not has_num: # Zero can't be the first digit, so it's invalid
                return False
            has_num = True # Saving that we encountered a number
        elif has_num and c.isalpha(): # If a number is followed by a letter, it's invalid
            return False
    return True

def check4(s):
    return s.isalnum() # .isalnum() checks if a string is only alphanumeric chars, which excludes punctuation and spaces


main()
