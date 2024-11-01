import requests
import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        sys.exit("Request exception")

    o = r.json()
    price = o["bpi"]["USD"]["rate_float"]

    cost = n * price

    print(f"${cost:,.4f}")

main()
