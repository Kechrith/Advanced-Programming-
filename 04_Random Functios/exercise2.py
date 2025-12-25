'''Write  a  program that  lets  the  user  guess  whether a  flipped  coin  displays the 
head or the tail. The program randomly generates head or tail. The program prompts the user to enter 
a  guess  and  reports  whether  the  guess  is  correct  or  incorrect.  Make  it  be  case  insensitive.  Here  are 
sample runs (for example, the random coin side is Head): '''
#import random module 
import random

# randomly choose head or tail
game = random.choice(["Head","Tail"])

#ask the player to guess head or tail 
player = input("Enter your guess(Head or Tail):")

#Check if the player input correct and convert all the letters to small
if player.lower() == game.lower():
    print("Correct😘")
#Check if the player input Incorrect
else:
    print("Incorrect😔")
