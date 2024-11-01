# In a file called figlet.py, implement a program that:
#
# Expects zero or two command-line arguments:
### Zero if the user would like to output text in a random font.
### Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.

# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
# the program should exit via sys.exit with an error message.

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1: # Only file name
    fontname = random.choice(figlet.getFonts())
    figlet.setFont(font=fontname)
elif len(sys.argv) == 3: # File name, '-f'/'--font' and fontname
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
text = input("Input: ")
print("Output:", figlet.renderText(text))
