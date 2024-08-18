import random

# Prompt the user for a level
# The int should be a positive integer
while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    if n <= 0:
        continue
    elif n >= 1:
        random_n = random.randint(1, n)
        while True:
            try:
                guess = int(input("Guess: "))
            except ValueError:
                continue
        # If the guess is smaller than the integer, "Too small!" and reprompt
            if guess < random_n:
                print("Too small!")
        # If the guess is larger than the integer, "Too large!" and reprompt
            elif guess > random_n:
                print("Too large!")
        # If the guess is the same as the integer, "Just right!" and exit
            else:
                print("Just right!")
                break
    break
