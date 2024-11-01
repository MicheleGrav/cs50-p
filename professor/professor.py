import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        s = x + y

        for attempt in range(3):
            try:
                res = int(input(f"{x} + {y} = "))
                if res == s:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

        if attempt == 2 and res != s:
            print(f"{x} + {y} = {s}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level not in [1, 2, 3]:
                raise ValueError
            else:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
