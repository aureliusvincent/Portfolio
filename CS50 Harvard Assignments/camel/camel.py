# list of name formats
name = ["name", "first_name", "preferred_first_name"]

# ask the user to input name
n = input("camelCase: ")

    # if the user inputs "name"
if n == "name":
    print("snake_case: " + name[0])
    # if the user inputs "firstName"
elif n == "firstName":
    print("snake_case: " + name[1])
    # if the user inputs "preferredFirstName"
elif n == "preferredFirstName":
    print("snake_case: " + name[2])
else:
    print()