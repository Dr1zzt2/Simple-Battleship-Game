import os
from random import randint
mode = 0
board = []
player1_ship_rows = [0,0,0]
player1_ship_cols = [0,0,0]
player2_ship_rows = [0,0,0]
player2_ship_cols = [0,0,0]
print("Welcome to our Battleship game.")
print("1. Singleplayer\n2. Multiplayer")
while mode < 1 or mode > 2:
    try:
        mode = int(input("Choose: "))
        os.system("clear")
    except ValueError:
        continue
for x in range(5):
    board.append(["O"] * 5)
def print_board(board):
    for row in board:
        print(" ".join(row))
def ship_pos_row():
    r = int(input("Row: "))
    return(r)
def ship_pos_col():
    c = int(input("Column: "))
    os.system("clear")
    return(c)
for x in range(3):
    print("Player 1 turn to place ship.")
    player1_ship_rows[x] = ship_pos_row()
    player1_ship_cols[x] = ship_pos_col()
    if mode == 2:
        print("Player 2 turn to place ship.")
        player2_ship_rows[x] = ship_pos_row()
        player2_ship_cols[x] = ship_pos_col()
    else:
        player2_ship_rows[x] = randint(0, len(board) - 1)
        player2_ship_cols[x] = randint(0, len(board[0]) - 1)

print("All ships have been placed.")
print(player2_ship_rows)
print(player2_ship_cols)

def shoot():
     
    while player1_ship_rows != [0,0,0,] or player2_ship_rows != [0,0,0] :
        print("Player 1's turn to shoot")
        guess_row = int(input(" Guess the row: "))
        guess_col = int(input(" Guess the column: "))
        os.system("clear")
        hit = False
        for x in range(3):
            if guess_row == player2_ship_rows[x] and guess_col == player2_ship_cols[x]:
                hit = True
                print("Player 1 hit a battleship!")
                player2_ship_rows[x] = 0
                player2_ship_cols[x] = 0
                print(player2_ship_rows)
        if hit != True:
            print("No hit")
        if mode == 2:
            print("Player 2's turn to shoot!")
            guess_row = int(input(" Guess the row: "))
            guess_col = int(input(" Guess the column: "))
            os.system("clear")
            hit = False
            for x in range(3):
                if guess_row == player1_ship_rows[x] and guess_col == player1_ship_cols[x]:
                    hit = True
                    print("Player 2 hit a battleship!")
                    player1_ship_rows[x] = 0
                    player1_ship_cols[x] = 0
        elif mode == 1:
            guess_row = randint(0,6)
            guess_col = randint(0,6)
            hit = False
            for x in range(3):
                if guess_row == player1_ship_rows[x] and guess_col == player1_ship_cols[x]:
                    hit = True
                    print("Player 2 hit a battleship!")
                    player1_ship_rows[x] = 0
                    player1_ship_cols[x] = 0
        if hit != True:
            print("No hit.")

shoot()
print_board()