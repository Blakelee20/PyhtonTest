import random
import sys
 
showDashes = False
 
# Add difficulties!
# Add letter-proof input!
 
board = [" ", " ", " ",  # 0, 1, 2
         " ", " ", " ",  # 3, 4, 5
         " ", " ", " "]  # 6, 7, 8
 
wins = [[0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 4, 8], [2, 4, 6]]             # Diagonal
 
_input = ""
 
def show():
    if showDashes == True: print("-------")
    print("|"+str(board[0])+"|"+str(board[1])+"|"+str(board[2])+"|")
    if showDashes == True: print("-------")
    print("|"+str(board[3])+"|"+str(board[4])+"|"+str(board[5])+"|")
    if showDashes == True: print("-------")
    print("|"+str(board[6])+"|"+str(board[7])+"|"+str(board[8])+"|")
    if showDashes == True: print("-------")
 
 
def checkline(char,spot1,spot2,spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        if char == "X":
            board[spot1] == "\u001b[1;31m" + char + "\u001b[0m"
            board[spot2] == "\u001b[1;31m" + char + "\u001b[0m"
            board[spot3] == "\u001b[1;31m" + char + "\u001b[0m"
            show()
            print("You Win!")
            sys.exit()
        if char == "O":
            board[spot1] == "\u001b[1;31m" + char + "\u001b[0m"
            board[spot2] == "\u001b[1;31m" + char + "\u001b[0m"
            board[spot3] == "\u001b[1;31m" + char + "\u001b[0m"
            show()
            print("You Suck! You Lose!")
            sys.exit()
 
 
def checkall(char):
    winning = 0
    for x in range(len(wins)):
        checkline(char, wins[x][0], wins[x][1], wins[x][2]) == True
 
 
def game():
    while True:
        _input = input("Choose a spot: ")
        _input = int(_input)
        if board[int(_input)] != 'X' and board[int(_input)] != 'O':
            board[(int(_input))] = 'X'
            checkall("X")
            finding = True
            while finding == True:
                random.seed()
                opponent = random.randint(0,8)
                if board[opponent] != 'O' and board[opponent] != 'X':
                    board[opponent] = 'O'
                    checkall("O")
                    finding = False
 
            show()
        else:
            print("This spot is taken!")
 
show()
game()