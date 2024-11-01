# In a file called pizza.py, implement a program that expects exactly one
# command-line argument, the name (or path) of a CSV file in Pinocchio’s format,
# and outputs a table formatted as ASCII art using tabulate,
# a package on PyPI at pypi.org/project/tabulate.
# Format the table using the library’s grid format.
# If the user does not specify exactly one command-line argument, or
# if the specified file’s name does not end in .csv, or
# if the specified file does not exist, the program should instead exit via sys.exit.

from tabulate import tabulate
import csv
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)

            if not data:
                sys.exit("No data in CSV file")

            headers = reader.fieldnames
            if headers is None:
                sys.exit("CSV file does not have headers")
    except FileNotFoundError:
        sys.exit("File not found")

    print(tabulate(data, headers = 'keys', tablefmt="grid"))
    # print("Data:", data)
    # print("Headers: ", headers)
if __name__ == "__main__":
    main()

