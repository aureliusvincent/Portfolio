def main():
    e = input("File name: ").casefold().strip()
    a = e.endswith(".gif")
    b = e.endswith(".jpg")
    c = e.endswith(".jpeg")
    d = e.endswith(".png")
    p = e.endswith(".pdf")
    t = e.endswith(".txt")
    z = e.endswith(".zip")
    if a:
        print("image/gif")
    elif b or c:
        print("image/jpeg")
    elif d:
        print("image/png")
    elif p:
        print("application/pdf")
    elif t:
        print("text/plain")
    elif z:
        print("application/zip")
    else:
        print("application/octet-stream")
main()