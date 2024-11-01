from datetime import date, datetime
import re
import sys
import inflect

def main():
    birth_date = input("Date of Birth: ")
    try:
        birth_date = parse_date(birth_date)
        minutes = calc_mins(birth_date)
        words = minutes_to_words(minutes)
        print(words, "minutes")
    except ValueError:
        sys.exit("Invalid date")

def parse_date(s):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        raise ValueError()
    return datetime.strptime(s, "%Y-%m-%d").date()

def calc_mins(bday):
    today = date.today()
    res = (today - bday).days
    return res * 24 * 60

def minutes_to_words(mins):
    p = inflect.engine()
    words = p.number_to_words(mins, andword="")
    return words.capitalize()

if __name__ == "__main__":
    main()
