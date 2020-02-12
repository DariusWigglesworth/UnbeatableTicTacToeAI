import random
import sys

humanWins = 0
programWins = 0
ties = 0
programFirst = True

board = [[None, "|", None, "|", None], [None, "|", None, "|", None], [None, "|", None, "|", None]]

def humanTurn():
    return 0

def programTurn():
    return 0

print("Welcome to the unbeatable tic-tac-toe machine\nYou have won ", humanWins, " to the programs ", programWins, "wins with ", ties, " ties")
print("Would you like to play the game? Y/N")

entered = input()
if entered.capitalize() != 'Y' or entered.capitalize() != 'N':
    print("Invalid input")
    sys.exit()
elif entered.capitalize() == "N":
    print("You won ", humanWins, " games, compared to the computers ", programWins, " wins! With ", ties, " ties.")
    print("Goodbye!")
    sys.exit()

if random.randrange(0, 1000) % 2 == 0:
    programFirst = True
    print("The program won the die roll and has chosen to go first")
else:
    print("You have won the die roll. Would you like to go first? Y/N")
    entered = input()
    if entered.capitalize() != 'Y' or entered.capitalize() != 'N':
        print("Invalid input")
        sys.exit()

print(board[0])
print("\n")
print("_ _ _\n")
print(board[1])
print("\n")
print("_ _ _\n")
print(board[2])