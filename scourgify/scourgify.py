import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    in_name = sys.argv[1]
    out_name = sys.argv[2]

    try:
        with open(in_name, "r") as filein:

            reader = csv.DictReader(filein)
            data = list(reader)

    except FileNotFoundError:
        sys.exit("Could not read", filein)

    try:
        with open(out_name, "w", newline='') as fileout:

            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(fileout, fieldnames=fieldnames)

            writer.writeheader()

            for row in data:
                name = row['name'].strip('"')
                last, first = name.split(", ")
                house = row['house']

                writer.writerow({'first': first, 'last': last, 'house': house})

    except Exception:
        sys.exit("Coult not write on", fileout)

if __name__ == "__main__":
    main()
