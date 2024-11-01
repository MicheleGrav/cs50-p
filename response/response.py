from validator_collection import validators, checkers, errors

def main():
    mail = input("What's your email address? ")
    is_email_address = checkers.is_email(mail)

    print("Valid" if is_email_address else "Invalid")

if __name__ == "__main__":
    main()
