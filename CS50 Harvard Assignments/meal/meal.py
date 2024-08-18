def main():
    time = input("What time is it? ")
    c_time = convert(time)
    if 7 <= c_time <= 8:
        print("breakfast time")
    elif 12 <= c_time <= 13:
        print("lunch time")
    elif 18 <= c_time <= 19:
        print("dinner time")


def convert(time):
    # 5:20, 5 to hours, 20 to minutes
    # challenge: ##:## am, ##:## pm
    # check if am is in the input
    if "a.m." in time or "p.m." in time:
        hours_minutes, pm_am = time.split(" ")
        hours, minutes = hours_minutes.split(":")
    # condition for pm and am
        if pm_am == "p.m." and int(hours) != 12:
            hours = int(hours) + 12
    # if am is in the input:
    else:
        hours, minutes = time.split(":") # let's the program to output 'am'
    # str to float conversion
    hours = float(hours) + (float(minutes) / 60)
    return hours


if __name__ == "__main__":
    main()