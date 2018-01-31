"""
This is a rock paper scissors game where you can play against the computer!
"""

import random

choices = ("rock", "paper", "scissors")

comp_choice = random.choice(choices)

your_choice = str(input("rock"))

print("You chose:")
print(your_choice)

print("The computer chose:")
print(comp_choice)

if your_choice == "rock" and comp_choice == "scissors" or\
   your_choice == "scissors" and comp_choice == "paper" or\
   your_choice == "paper" and comp_choice == "rock":
    print("Congratulations, You won!")
elif your_choice == "rock" and comp_choice == "scissors" or\
        your_choice == "scissors" and comp_choice == "paper" or\
        your_choice == "paper" and comp_choice == "rock":
    print("Bad luck, You lost!")
elif your_choice == comp_choice:
    print("It is a tie!")