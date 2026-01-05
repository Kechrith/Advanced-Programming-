'''
Group 9
Write  a  program  that  plays  the  popular  scissor-rock-paper  game.  (A 
scissor  can  cut  a  paper,  a  rock  can  knock  a  scissor,  and  a  paper  can  wrap  a  rock.)  The  program 
randomly generates scissor, rock, or paper. The program asks the user to enter scissor, rock, or paper 
and displays a message indicating whether the user wins, loses, or draws. '''
#import random module 
import random

# randomly choose 
game = random.choice(["scissor",  "rock",  "paper"])

#ask the player to guess and convert all the letters to small
player = input("Enter your guess( scissor, rock or paper):").lower()

# show both choices
print("The computer is", game)
print("You are", player)

# check if both choices are the same
if player == game:
    print("It is a draw")
# check all winning conditions for the user
elif (
    (player == "scissor" and game == "paper") or
    (player == "rock" and game == "scissor") or
    (player == "paper" and game == "rock")
):
    print("You won")
#Check if the player lose
else:
    print("You Lose")
