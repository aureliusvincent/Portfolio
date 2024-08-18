def main():
    # ask the user to enter alphanumeric characters
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# conditions are:
    # vanity plates must start with at least two characters
    # vanity plates may contain a max number of 6 characters and a min of 2 characters
    # numbers cannot be used in the middle of a plate
    # no periods, spaces, or punctuation marks are allowed
def is_valid(s):
    # char length between 2-6 chars, starts with 2 chars, and alnum
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        # checking numeric characters
        for num in s:
            # create a condition for numeric characters
            if num.isdigit():
                # create a variable for numeric characters so that it can be sliced
                index = s.index(num)
                # check if the numbers are in the middle of a plate
                # and check if it starts with 0
                if s[index:].isdigit() and int(num) != 0:
                    return True
                else:
                    return False
        return True



main()