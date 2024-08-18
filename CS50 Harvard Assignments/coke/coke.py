# coke vending machine that sells a coke for 50 cents
print("Amount Due: 50")

# set variables
amount_due = 50
coins_added = 0
# ask the user to insert a coin
while True:
    insert_coin = int(input("Insert Coin: "))
# the machine accepts coins in these denominations: 25 cents, 10 cents, 5 cents
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_due -= insert_coin
        coins_added += insert_coin
    else:
        print(f"Amount Due: {amount_due}")
# if the user inserted a coin more than 50
    if coins_added >= 50:
        print(f"Change Owed: {coins_added - 50}")
        break
# if the user inserted a coin other than the denominators
    else:
        print(f"Amount Due: {amount_due}")