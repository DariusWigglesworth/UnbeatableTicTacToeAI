import random
import sys

humanWins = 0
programWins = 0
ties = 0
programFirst = True

# board = [[None, "|", None, "|", None], [None, "|", None, "|", None], [None, "|", None, "|", None]]
# board = [[" ", "|", " ", "|", " "], [" ", "|", " ", "|", " "], [" ", "|", " ", "|", " "]]
# for entry in board:
#     for entry2 in entry:
#         print(entry2)

board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
spotTaken = [False, False, False, False, False, False, False, False, False]

def printBoard():
    for entry in board:
        for space in entry:
            print(space, end=" ")
        print("\n")
    return 0

def inputTo2D(humanInput):
    if humanInput < 4:
        board[0][humanInput - 1] = "X"
    elif humanInput < 7:
        board[1][humanInput - 4] = "X"
    else:
        board[2][humanInput - 7] = "X"
    return 0

def humanTurn():
    print("It's your turn to go! Here's the board so far:")
    printBoard()
    entered = input("Please enter the number of the space that you would like to go: ")
    entered = int(entered)
    
    if (entered <= 0) or (entered >= 10) or (spotTaken[entered] == True):
        print("Invalid input, try again")
        humanTurn()
    
    inputTo2D(entered)
    spotTaken[entered] = True
    printBoard()
    return 0

def programTurn():
    return 0

# print(board[0])
# print("_ _ _\n")
# print(board[1])
# print("_ _ _\n")
# print(board[2])

printBoard()

print("Welcome to the unbeatable tic-tac-toe machine\nYou have won ", humanWins, " to the programs ", programWins, "wins with ", ties, " ties")
entered = input("Would you like to play the game? Y/N: ")

if (entered.capitalize() != 'Y') and (entered.capitalize() != 'N'):
    print("Invalid input")
    sys.exit()
elif entered.capitalize() == "N":
    print("You won ", humanWins, " games, compared to the computers ", programWins, " wins! With ", ties, " ties.")
    print("Goodbye!")
    sys.exit()

# if (random.randrange(0, 1000) % 2 == 0):
if (False == True):
    programFirst = True
    print("The program won the die roll and has chosen to go first")
    programTurn()
else:
    entered = input("You have won the die roll. Would you like to go first? Y/N: ")
    if entered.capitalize() != 'Y' and entered.capitalize() != 'N':
        print("Invalid input")
        sys.exit()
    humanTurn()

# print(board[0])
# print("\n")
# print("_ _ _\n")
# print(board[1])
# print("\n")
# print("_ _ _\n")
# print(board[2])