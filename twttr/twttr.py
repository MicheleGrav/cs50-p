# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
# much like Twitter was originally called twttr.
# In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs
# that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    str1 = input("Input: ")
    str2 = twttfy(str1)
    print(f"Output: {str2}")

# Function to manage vowel removal
def twttfy(s1):
    s2 = ""
    for i in s1:
        if not vowel_check(i):
            s2 += i # Append only if not a vowel
    return s2

# Function that checks if a letter is a vowel
def vowel_check(c):
    return c.lower() in ['a', 'e', 'i', 'o', 'u'] # .lower() to check uppercase and lowercase

main()
