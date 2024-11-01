import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s.startswith("<iframe"):
        m = re.search(r"(http|https)://(www\.)?youtube\.com/embed/([-a-zA-Z0-9_]+)", s)

        if m:
            id = m.group(3)
            return f"https://youtu.be/{id}"
    return None

if __name__ == "__main__":
    main()
