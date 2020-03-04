import random
import sys

humanWins = 0
programWins = 0
ties = 0

board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
spotTaken = [False, False, False, False, False, False, False, False, False]
humanSpots = [False, False, False, False, False, False, False, False, False]
programSpots = [False, False, False, False, False, False, False, False, False]

firstTurn = True

def checkWin(player):
    winner = False

    if (programSpots[0] and programSpots[1] and programSpots[2]) or (programSpots[3] and programSpots[4] and programSpots[5]) or (programSpots[6] and programSpots[7] and programSpots[8]):
        winner = True
    elif (programSpots[0] and programSpots[3] and programSpots[6]) or (programSpots[1] and programSpots[4] and programSpots[7]) or (programSpots[2] and programSpots[5] and programSpots[8]):
        winner = True
    elif (programSpots[0] and programSpots[4] and programSpots[8]) or (programSpots[2] and programSpots[4] and programSpots[6]):
        winner = True
    elif (humanSpots[0] and humanSpots[1] and humanSpots[2]) or (humanSpots[3] and humanSpots[4] and humanSpots[5]) or (humanSpots[6] and humanSpots[7] and humanSpots[8]):
        winner = True
    elif (humanSpots[0] and humanSpots [3] and humanSpots[6]) or (humanSpots[1] and humanSpots[4] and humanSpots[7]) or (humanSpots[2] and humanSpots[5] and humanSpots[8]):
        winner = True
    elif (humanSpots[0] and humanSpots[4] and humanSpots[8]) or (humanSpots[2] and humanSpots[4] and humanSpots[6]):
        winner = True

    if winner:
        firstTurn = True
        if player == "Human":
            print("Congratulations on winning!")
            humanWins = humanWins + 1
        else:
            print("The program won!")
            programWins = programWins + 1
        return 1
    
    return 0

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
    firstTurn = False
    print("It's your turn to go! Here's the board so far:")
    printBoard()
    entered = input("Please enter the number of the space that you would like to go: ")
    entered = int(entered)
    
    if (entered <= 0) or (entered >= 10) or (spotTaken[entered] == True):
        print("Invalid input, try again")
        humanTurn()
    
    inputTo2D(entered)
    spotTaken[entered] = True
    humanSpots[entered] = True
    printBoard()
    checkWin("Human")

    return 0

def programTurn():
    firstTurn = False
    return 0

printBoard()

while(True):
    if firstTurn:
        print("Welcome to the unbeatable tic-tac-toe machine\nYou have won ", humanWins, " to the programs ", programWins, "wins with ", ties, " ties")
        entered = input("Would you like to play the game? Y/N: ")

        if (entered.capitalize() != 'Y') and (entered.capitalize() != 'N'):
            print("Invalid input")
            # sys.exit()
        elif (entered.capitalize() == "N"):
            print("You won ", humanWins, " games, compared to the computers ", programWins, " wins! With ", ties, " ties.")
            print("Goodbye!")
            sys.exit()

        # if (random.randrange(0, 1000) % 2 == 0):
        elif (False == True): #Temp so human always goes first (testing purposes)
            print("The program won the die roll and has chosen to go first")
            programTurn()
        else:
            entered = input("You have won the die roll. Would you like to go first? Y/N: ")
            if entered.capitalize() != 'Y' and entered.capitalize() != 'N':
                print("Invalid input")
                sys.exit()
            humanTurn()
    humanTurn()
    programTurn()