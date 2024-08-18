def main():
    expression = input("Expression: ")
    x = int
    y = "+" or "-" or "*" or "/"
    z = int
    x, y, z = expression.split(" ")

    a = str(int(x) + int(z))
    b = str(int(x) - int(z))
    c = str(int(x) * int(z))
    d = int(x) / int(z)

    if y == "+":
        print(a + ".0")
    elif y == "-":
        print(b + ".0")
    elif y == "*":
        print(c + ".0")
    else:
        print(round(d, 1))

main()
