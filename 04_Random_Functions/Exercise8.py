"""(Simulation firing a gun) For this game, six players will play together. Five bullets are put into a gun's 
round barrel which can hold up to six bullets.A staff from the game will start pointing the gun at the first player and firing the gun. If no  bullet is 
fired,  the  player  survives,  otherwise,  the  player  gets  shot  and  die.  The  staff  will  do  the  same  to  all 
players one by one. Note that the staff will roll the barrel before each shooting.  
Which  turn  (1st  to  6th)  would  you  choose  to  increase  your  chance  of  survival?  To  answer  this 
question,  write  a  program  to  simulate  this  gun shooting  game  one  thousand  rounds,  and  display  the 
number of each player getting shot based on the turn they take to get shot. """
import random

#Store the number of times each player gets shot
shots = [0, 0, 0, 0, 0, 0]

#Repeat the game one thousand times
for _ in range(1000):
    barrel = [1, 1, 1, 1, 1, 0]

    #Each player takes a turn
    for i in range(6):
        random.shuffle(barrel)

        #If the player gets shot
        if barrel[0] == 1:
            shots[i] += 1
            break
        
#Display the results 
for i in range(6):
    print("Player", i + 1, "gets shot", shots[i], "times")
