#Python Tic-Tac-Toe Game
import random
import collections as c
import os
import time
#The game board
board = b = list(range(1,10))

rows = ['012', '345', '678']
columns = ['036', '147', '258']
X = ['048', '246']

def show_Board(): #Displays game board
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])
    print('')

def getrow(space): #Gets the row of a space
    for i in range(3):
        if str(space) in rows[i]:
            return(i)

def getcolumn(space): #Gets the column of a space
    for i in range(3):
        if str(space) in columns[i]:
            return(i)

def getX(space): #Gets the diagonal of a space, and checks if center
    if space == 4:
        return(2)
    for i in range(2):
        if str(space) in X[i]:
            return(i)

def check_Row(space): #Checks for X's and for empty spaces in row
    RS = rows[getrow(space)]
    ARS = []
    if 'X' not in set(b[int(RS[i])] for i in range(3)):
        for i in RS:
            if board[int(i)] != 'O':
                ARS.append(i)
    return(ARS)

def check_Column(space): #Checks for X's and for empty spaces in column
    CS = columns[getcolumn(space)]
    ACS = []
    if 'X' not in set(b[int(CS[i])] for i in range(3)):
        for i in CS:
            if board[int(i)] != 'O':
                ACS.append(i)
    return(ACS)

def check_Center(): #Checks for X's and for empty spaces in both diagonals
    ACS = []
    if 'X' not in set(b[int(X[0][i])] for i in range(3)):
        for i in X[0]:
            if board[int(i)] != 'O':
                ACS.append(i)
    if 'X' not in set(b[int(X[1][i])] for i in range(3)):
        for i in X[1]:
            if board[int(i)] != 'O':
                ACS.append(i)
    return(ACS)

def check_X(space): #Checks for X's and for empty spaces in diagonal
    AXS = []
    if getX(space) == 2:
        for i in check_Center():
            AXS.append(i)
        return(AXS)
    
    XS = X[getX(space)]
    
    if 'X' not in set(b[int(XS[i])] for i in range(3)):
        for i in XS:
            if board[int(i)] != 'O':
                AXS.append(i)
    return(AXS)

def scan_Board(): #Checks for open spaces
    openspaces = osp = []
    for space in range(9):
        if board[space] == 'O':
            if check_Row(space) != None:
                for i in check_Row(space):
                    osp.append(int(i))
            if check_Column(space) != None:
                for i in check_Column(space):
                    osp.append(int(i))
            if getX(space) != None:
                if check_X(space) != None:
                    for i in check_X(space):
                        osp.append(int(i))
        if all(isinstance(spaces, int) for spaces in board):
            osp.append(space)
    return openspaces

def can_Win(player): #Checks if (player) has 2-in-a-row
    for row in rows:
        if list(board[int(row[i])] for i in range(3)).count(player) == 2:
            for i in row:
                if isinstance(board[int(i)], int):
                    return(int(i))
    for column in columns:
        if list(board[int(column[i])] for i in range(3)).count(player) == 2:
            for i in column:
                if isinstance(board[int(i)], int):
                    return(int(i))
    for diag in X:
        if list(board[int(diag[i])] for i in range(3)).count(player) == 2:
            for i in diag:
                if isinstance(board[int(i)], int):
                    return(int(i))          
    return(None)
          
def player_Move(mark): #Player's turn 
    while True:
        while True:
            try:
                move = int(input("Select a spot: "))
                break
            except ValueError:
                print("Input an available number from the board.")
        if int(move) not in board:
            print("Number out of range. Choose an available spot on the board.")
            continue
        else:
            move = int(move) - 1
        
        if board[move] != 'X' and board[move] != 'O':
            board[move] = mark
            break

        else:
            print("Spot already taken. Select another.")
            continue

def com_Move(): #Computer's turn. Computer scans board and picks from the best possible spaces.
    while True:
        if can_Win('O') != None: #Go for the win if possible!
            board[(can_Win('O'))] = 'O'
            break
        if can_Win('X') != None: #Block player from winning!
            board[can_Win('X')] = 'O'
            break
                    
        openspaces = osp = scan_Board()
        bestspaces = bs = []
        count = c.Counter(osp) #Counts how many 'points' each space has
        #print(openspaces)
        if not openspaces:
            for i in range(9):
                if isinstance(board[i], int):
                    board[i] = 'O'
                    break
            break
        if 3 in count.values():
            for k,v in count.items():
                if v == 3:
                    bs.append(k)
            board[random.choice(bs)] = 'O'
            break
        if 2 in count.values():
            for k,v in count.items():
                if v == 2:
                    bs.append(k)
            board[random.choice(bs)] = 'O'
            break
        else:
            board[random.choice(osp)] = 'O'
            break

def win_Check(): #Checks for 3-in-a-row
    for row in rows:
        lst = list(board[int(row[i])] for i in range(3))
        if lst[1:] == lst[:-1]:
            return True
    for column in columns:
        lst = list(board[int(column[i])] for i in range(3))
        if lst[1:] == lst[:-1]:
            return True
    for diag in X:
        lst = list(board[int(diag[i])] for i in range(3))
        if lst[1:] == lst[:-1]:
            return True
    else:
        return False

def player_Turn(mark, player):
    os.system('cls')
    print(player + "'s move...")
    show_Board()
    player_Move(mark)

def computer_Turn():
    os.system('cls')
    print("Computer's move...")
    show_Board()
    time.sleep(2)
    os.system('cls')
    com_Move()
#------------------------------------------------------------------------------
while True:
    gamemode = input("PvP or PvC? ")
    if gamemode != "PvP" and gamemode != "PvC":
        print("Please choose a valid game mode.")
        continue
    break
if gamemode == 'PvC':
    if random.randrange(0,100) > 50: #Randomly selects who starts
        for i in range(5):
            player_Turn('X', 'Player')
            if win_Check() == True:
                os.system('cls')
                print("You won the game!")
                show_Board()
                break
            if i == 4:
                os.system('cls')
                print("It's a cat's game!")
                show_Board()
                break
            computer_Turn()
            if win_Check() == True:
                os.system('cls')
                print("Computer won the game!")
                show_Board()
                break
    else:
        for i in range(5):
            computer_Turn()
            if win_Check() == True:
                os.system('cls')
                print("Computer won the game!")
                show_Board()
                break
            if i == 4:
                os.system('cls')
                print("It's a cat's game!")
                show_Board()
                break
            player_Turn('X', 'Player')
            if win_Check() == True:
                os.system('cls')
                print("You won the game!")
                show_Board()
                break
            
if gamemode == 'PvP':
    for i in range(5):
            player_Turn('O', 'Player 1')
            if win_Check() == True:
                os.system('cls')
                print("Player 1 won the game!")
                show_Board()
                break
            if i == 4:
                os.system('cls')
                print("It's a cat's game!")
                show_Board()
                break
            player_Turn('X', 'Player 2')
            if win_Check() == True:
                os.system('cls')
                print("Player 2 won the game!")
                show_Board()
                break
input()
