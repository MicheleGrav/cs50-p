import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError")
        sys.exit(1)

def convert(s):
    m = re.match(r"(\b\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\b\d{1,2})(?::(\d{2}))?\s+(AM|PM)\b", s)

    if not m:
        raise ValueError()

    first_hour = int(m.group(1))
    first_minute = m.group(2)
    first_period = m.group(3)

    second_hour = int(m.group(4))
    second_minute = m.group(5)
    second_period = m.group(6)

    if first_minute is None:
        first_minute = '00'
    first_hour = convert_24h(first_hour, first_minute, first_period)

    if second_minute is None:
        second_minute = '00'
    second_hour = convert_24h(second_hour, second_minute, second_period)

    return f"{first_hour:02d}:{first_minute} to {second_hour:02d}:{second_minute}"

def convert_24h(h, m, p):
    h = int(h)
    m = int(m)

    if m < 0 or m >= 60:
        raise ValueError()

    if p == 'AM':
        if h == 12:
            return 0
    elif p == 'PM':
        if h != 12:
            h += 12

    return h

if __name__ == "__main__":
    main()

