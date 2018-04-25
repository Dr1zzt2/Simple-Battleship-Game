import os
from random import randint
mode = 0
board = []
board2 = []
player1_ship_rows = [0,0,0] # listaception for more ships -> [0,[0,0],0,0]
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
    board.append(["0"] * 5)
    board2.append(["0"] * 5)
def print_board(board):
    for row in board:
        print(" ".join(row))
def print_board2(board2):
    for row in board2:
        print(" ".join(row))
def ship_pos_row():
    r = 0
    while r > 5 or r < 1:
        try:
            r = int(input("Row: "))
        except ValueError:
            os.system("clear")
            continue
    return(r-1)
def ship_pos_col():
    c = 0
    while c > 5 or c < 1:
        try:
            c = int(input("Column: "))
        except ValueError:
            os.system("clear")
            continue
    os.system("clear")
    return(c-1)
def guess_rows():
    global guess_row
    guess_row = 0
    while guess_row > 5 or guess_row < 1:
        try:
            guess_row = int(input(" Guess the row: "))
        except ValueError:
            os.system("clear")
            continue
def guess_columns():
    global guess_col
    guess_col = 0
    while guess_col > 5 or guess_col < 1:
        try:
            guess_col = int(input(" Guess the column: "))
        except ValueError:
            os.system("clear")
            continue
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
    global guess_row
    global guess_col
    while True: 
        print("Player 1's turn to shoot")
        print_board2(board2)
        guess_rows()
        guess_row -= 1
        guess_columns()
        guess_col -= 1
        os.system("clear")
        hit = False
        if board2[guess_row][guess_col] == "0":
            for x in range(3):
                if guess_row == player2_ship_rows[x] and guess_col == player2_ship_cols[x]:
                    hit = True
                    print("Player 1 hit a battleship!")
                    board2[guess_row][guess_col] = "X"
                    player2_ship_rows[x] = -1
                    player2_ship_cols[x] = -1
                    print(player2_ship_rows)
                    break
                    
            if player2_ship_rows == [-1,-1,-1,]:
                break
        elif board2[guess_row][guess_col] == "X":
            print("You already destroyed that ship!")
            continue
        elif board2[guess_row][guess_col] == "-":
            print ("You already shot there.")
            continue
        if hit != True and board2[guess_row][guess_col] != "X":
            print("Player 1 misses.")
            board2[guess_row][guess_col] = "-"
            break
    while True:     
        if mode == 2:
            print("Player 2's turn to shoot!")
            print_board(board)
            guess_rows()
            guess_row -= 1
            guess_columns()
            guess_col -= 1
            os.system("clear")
            hit = False
            if board[guess_row][guess_col] == "0":
                for x in range(3):
                    if guess_row == player1_ship_rows[x] and guess_col == player1_ship_cols[x]:
                        hit = True
                        print("Player 2 hit a battleship!")
                        board[guess_row][guess_col] = "X"
                        player1_ship_rows[x] = -1
                        player1_ship_cols[x] = -1
                        break
                if player1_ship_rows == [-1,-1,-1]:
                    break
            elif board[guess_row][guess_col] == "X":
                print("You already destroyed that ship!")
                continue
            elif board[guess_row][guess_col] == "-":
                print ("You already shot there.")
                continue
        elif mode == 1:
            while True:
                guess_row = randint(0,4)
                guess_col = randint(0,4)
                if board[guess_row][guess_col] == "0":
                    break
            hit = False
            for x in range(3):
                if guess_row == player1_ship_rows[x] and guess_col == player1_ship_cols[x]:
                    hit = True
                    print("Player 2 hit a battleship!")
                    board[guess_row][guess_col] = "X"
                    player1_ship_rows[x] = -1
                    player1_ship_cols[x] = -1
                    break
                    
            if player1_ship_rows == [-1,-1,-1]:
                break
        if hit != True and board[guess_row][guess_col] != "X":
            print("Player 2 misses.")
            board[guess_row][guess_col] = "-"
            break

shoot()
if player1_ship_rows == [-1,-1,-1]:
    print("Player 2 Wins!")
if player2_ship_rows == [-1,-1,-1]:
    print("Player 1 Wins!")