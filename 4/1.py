import pyfiglet
from colorama import Fore, Back, Style, init
import time
import random

# Initialize colorama
init(autoreset=True)

# Function to display the game board
def show():
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == "X":
                print(Fore.GREEN + game_board[i][j], end="")
            elif game_board[i][j] == "O":
                print(Fore.BLUE + game_board[i][j], end="")
            else:
                print(game_board[i][j], end="")
        print()

# Function to check for a win
def check_game():
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] and game_board[i][0] != '-':
            return True

    for i in range(3):
        if game_board[0][i] == game_board[1][i] == game_board[2][i] and game_board[0][i] != '-':
            return True

    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] != '-':
        return True

    if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] != '-':
        return True

    return False

# Function to check for a tie
def is_board_full():
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == '-':
                return False
    return True

# Function for player vs player mode
def player_vs_player():
    while True:
        print("Player 1")
        while True:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    break
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Invalid input. Please enter valid row and col.")

        show()
        if check_game():
            print(Fore.GREEN + "Player 1 wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break

        print("Player 2")
        while True:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "O"
                    break
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Invalid input. Please enter valid row and col.")

        show()
        if check_game():
            print(Fore.BLUE + "Player 2 wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break

# Function for player vs CPU mode
def player_vs_cpu():
    while True:
        print("Player")
        while True:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    break
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Invalid input. Please enter valid row and col.")

        show()
        if check_game():
            print(Fore.GREEN + "Player wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break

        print("CPU")
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                print("CPU chooses row", row, "and col", col)
                break

        show()
        if check_game():
            print(Fore.BLUE + "CPU wins!")
            break
        if is_board_full():
            print("It's a tie!")
            break

# Main function to start the game
def play_game():
    global game_board
    game_board = [["-", "-", "-"],
                  ["-", "-", "-"],
                  ["-", "-", "-"]]

    title = pyfiglet.figlet_format("Tic Tac Toe", font='slant')
    print(title)

    print("Select mode:")
    print("1. Player vs Player")
    print("2. Player vs CPU")
    mode = input("Enter 1 or 2: ")

    if mode == "1":
        player_vs_player()
    elif mode == "2":
        player_vs_cpu()
    else:
        print("Invalid choice. Please try again.")

# Measure elapsed time for the game
start_time = time.time()
play_game()
end_time = time.time()

elapsed_time = end_time - start_time
print("Elapsed time: {:.2f} seconds".format(elapsed_time))

