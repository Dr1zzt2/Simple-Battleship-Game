m = 0
print("Welcome to our Battleship game.")
print("1. Singleplayer\n2. Multiplayer")
while m < 1 or m > 2:
    try:
        m = int(input("Choose "))
    except ValueError:
        continue