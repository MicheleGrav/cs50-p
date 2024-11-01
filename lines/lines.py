# In a file called lines.py, implement a program that expects exactly one command-line
# argument, the name (or path) of a Python file, and outputs the number of lines of
# code in that file, excluding comments and blank lines.
# If the user does not specify exactly one command-line argument, or
# if the specified file’s name does not end in .py, or
# if the specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace,
# is a comment. (A docstring should not be considered a comment.)
# Assume that any line that only contains whitespace is blank.
import sys

def main():
    count = 0

    # Managing wrong command-line args usage
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    # Checking file extension
    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()

                if not line.startswith("#") and line != "":
                    count += 1
    except FileNotFoundError: # Catching exception
        sys.exit("File does not exist")

    print(count)



if __name__ == "__main__":
    main()
