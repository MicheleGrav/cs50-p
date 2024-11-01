# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
# much like Twitter was originally called twttr.
# In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs
# that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    str1 = input("Input: ")
    str2 = shorten(str1)
    print(f"Output: {str2}")

# Function to manage vowel removal
def shorten(word):
    s2 = ""
    for c in word:
        if c.lower() not in ['a', 'e', 'i', 'o', 'u']:
            s2 += c # Append only if not a vowel
    return s2

if __name__ == "__main__":
    main()
