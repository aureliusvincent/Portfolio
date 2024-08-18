def main():
    g = input("Greetings: ").casefold().strip()
    if g.startswith("hello"):
        print("$0")
    elif g.startswith("h"):
        print("$20")
    else:
        print("$100")

main()