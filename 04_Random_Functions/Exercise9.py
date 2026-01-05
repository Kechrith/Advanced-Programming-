""" 
(Simulation picking a pearl) A screen flashes in front of you and explains you the game. There are six 
pearls (three are white and three are black) and two empty bowls. You are asked to divide all pearls 
into the two bowls in whatever way you like as long as each bowl has at least one pearl. Once you are 
done, the room will turn pitch black. The bowls will move and shuffle around. In the dark where you 
can see nothing, you have to pick up one pearl from any bowl. If the pearl you have in your hand is 
white,  you  will  be  allowed  to  live,  but  if the  pearl  you  picked  is  black,  the  room  will  be  filled  with 
poisonous gas and you will die.   
How would you divide the pearls to increase your chances of survival? To answer this question, write 
a program that simulates you picking a pearl one hundred times for each of every possible choice you 
can make. Display the number of your survival in each of your choice.
"""

import random 

# Total pearls: 3 white, 3 black
pearls = ["W", "W", "W", "B", "B", "B"]

# All possible valid ways to divide pearls into two bowls
choices = [
    (["W"], ["W", "W", "B", "B", "B"]),
    (["B"], ["W", "W", "W", "B", "B"]),
    (["W", "W"], ["W", "B", "B", "B"]),
    ((["W", "B"]), (["W", "W", "B", "B"])),
    (["B", "B"], ["W", "W", "W", "B"]),
    (["W", "W", "W"], ["B", "B", "B"])
]

choice_number = 1

# Go through each possible way of dividing pearls
for bowl1, bowl2 in choices:

    survival = 0   

    # Simulate picking pearls 100 times
    for i in range(100):

        # Randomly choose one of the bowls
        bowl = random.choice([bowl1, bowl2])

        # Randomly choose one pearl from that bowl
        pearl = random.choice(bowl)

        # If the pearl is white, we survive
        if pearl == "W":
            survival += 1

    # Display result for this choice
    print("Choice", choice_number, ":", bowl1, "and", bowl2,
          ", the number of survival is", survival, "/ 100 times")

    # Move to next choice
    choice_number += 1
