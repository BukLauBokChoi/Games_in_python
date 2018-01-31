"""
this is a rock paper scissors game where you can play against your friend!
"""


def Play_game():
    # players
    player1_name = str(input("What is your name?"))
    player2_name = str(input("What is your name?"))

    player1 = str(input("Player 1 chose :"))
    player2 = str(input("Player 2 chose :"))



    if player1 == player2:
        print("it's a tie")
    elif player1 == "paper" and player2 == "rock" or player1 == "rock" and player2 == "scissors" or player1 == "scissors" and player2 == "paper":
        print(f"{player1_name} won the game!")
    else:
        print(f"{player2_name} won the game!")


# how many times do you want to play
rounds = int(input("How many times do you want to play?"))

for i in range(rounds):
    Play_game()
