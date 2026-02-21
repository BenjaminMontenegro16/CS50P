while True:
    try:
        import random

        coin = random.choice(["Heads", "Tails"])

        print(coin)

    except EOFError :
        print("End of program")