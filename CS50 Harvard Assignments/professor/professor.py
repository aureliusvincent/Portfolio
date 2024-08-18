import random


def main():
    ...


def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        if n >= 3 or n <= 1:
            continue
        elif 1 <= n <= 3:
            raise ValueError
        break


def generate_integer(level):
    if n = 1:
        math = random.randint(1,10) + random.randint(1,10)
        if answer


if __name__ == "__main__":
    main()