def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    return float(d.removeprefix('$')) # String method .removeprefix() to get rid of dollarsign


def percent_to_float(p):
    # TODO
    return float(p.removesuffix('%')) / 100 #String method .removesuffix() to get rid of percentage, then /100 because it's a percentage


main()
