
import os

# Title
def header():
    print("""
    Tic Tac Toe game in python! 
    This is the board:  0|1|2
                        3|4|5
                        6|7|8
                        """)


# The board
Board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# Draw the board
def print_board():

    print(" " + Board[0] + " | " +  Board[1]  + " | " +  Board[2])
    print("---|---|---")
    print(" " + Board[3] + " | " +  Board[4]  + " | " +  Board[5])
    print("---|---|---")
    print(" " + Board[6] + " | " +  Board[7]  + " | " +  Board[8])


# check if anyone won
def is_winner(board, player):
    if Board[0] == player and Board[1] == player and Board[2] == player or \
       Board[3] == player and Board[4] == player and Board[5] == player or \
       Board[6] == player and Board[7] == player and Board[8] == player or \
       Board[0] == player and Board[3] == player and Board[6] == player or \
       Board[1] == player and Board[4] == player and Board[7] == player or \
       Board[2] == player and Board[5] == player and Board[8] == player or \
       Board[0] == player and Board[4] == player and Board[8] == player or \
       Board[2] == player and Board[4] == player and Board[6] == player:
       return True
    return False

# check if the board is full
# if it is  then it is a tie
def is_board_full(board):
    if " " in Board:
        return False
    return True

# update the screen
def update_screen():
    os.system("clear")
    print(header())
    print(print_board())

while True:
    # print the screen
    update_screen()

    "---------------------------------------------------------------------------------------"
    
    # Player X
    # choose the place you want to put X
    choice = int(input("Where do you want to put X? "))

    # check if it is a valid place
    if choice <= 9:
        # Check if space is empty
        if Board[choice] == " ":
            # If it is, add that to the board
            Board[choice] = "X"
        else:
            print("Sorry, that space is not empty! Please put it somewhere else.")
            os.system("say 'Sorry, that space is not empty! Please put it somewhere else.'")

    else:
        print("Sorry, you didn't choose a valid space!")
        os.system("say 'Sorry, you didn't choose a valid space!'")

    # Check if X has won
    # Check the rows, columns and diagnoals
    if is_winner(Board, "X"):
        # update the board
        update_screen()

        # End the game
        print("Congratulations! Player X has won the game!")
        os.system("say 'Congratulations! Player X has won the game!'")
        # ask if they want to play again
        print("Do you want to play again? (Y/N): ")
        play_again = str(input("")).upper()

        # reset the screen if they want to play again
        if play_again == "Y":
            Board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            os.system("clear")
            print(header())
            print(print_board())
        else:
            break

    # Update the screen
    update_screen()


    # Check for a tie
    # We assume that the board is full
    is_full = True
    # We want to prove that the board isn't full
    # Check all of the spaces in the board
    if is_board_full(Board):
    # Do something if the board is full
        print("It's a tie!")
        os.system("say 'It is a tie'")
        # ask if they want to play again
        print("Do you want to play again?(Y/N): ")
        play_again = str(input(""))
    
        # reset the screen if they want to play again
        if play_again == "Y":
            Board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            os.system("clear")
            print(header())
            print(print_board())
        else:
            break
    "---------------------------------------------------------------------------------------"

    # Player O
    # choose the place you want to put O
    choice = int(input("Where do you want to put O? "))

    # check if it is a valid space
    if choice <= 9:
        # Check if space is empty
        if Board[choice] == " ":
            # If it is, add that to the board
            Board[choice] = "O"
        else:
            print("Sorry, that space is not empty! Please put it somewhere else.")
            os.system("say 'Sorry, that space is not empty! Please put it somewhere else.'")

    else:
        print("Sorry, you didn't choose a valid space!")
        os.system("say 'Sorry, you didn't choose a valid space!'")

    # Check if O has won
    # Check the rows, columns and diagnoals
    if is_winner(Board, "O"):
        # update the board
        update_screen()

        # End the game
        print("Congratulations! Player O has won the game!")
        os.system("say 'Congratulations! Player O has won the game!'")
        print("Do you want to play again? (Y/N): ")
        play_again = str(input(""))

        # reset the screen if they want to play again
        if play_again == "Y":
            Board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            os.system("clear")
            print(header())
            print(print_board())
        else:
            break
    # Update the screen
    update_screen()

    # Check for a tie
    # We assume that the board is full
    is_full = True
    # We want to prove that the board isn't full
    # Check all of the spaces in the board
    if is_board_full(Board):
    # Do something if the board is full
        print("It's a tie!")
        # ask if they want to play again
        print("Do you want to play again?(Y/N): ")
        play_again = str(input(""))
    
        # reset the screen if they want to play again
        if play_again == "Y":
            Board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            os.system("clear")
            print(header())
            print(print_board())
        else:
            break
