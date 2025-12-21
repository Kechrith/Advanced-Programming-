"""(Game: locker puzzle) There are 50 lockers and 50 players. When the game starts, all the lockers are 
closed.  As  the  players  enter  the  building,  the  first  player  (P1)  has  to  open  every  locker.  Then  the 
second  player  (P2)  begins  with  the  second  locker  (L2),  and  has  to  close  every  other  locker  (L2  to 
L50). Player P3 begins with the third locker (L3) and has to change (closes the locker if it was open, 
and  open  it if it was closed) every third locker (L3, L6, ...). Player P4 begins with locker L4 and 
changes every fourth locker (L4, L8, ...), and so on, until Player P50 changes L50.  
Write  a  program  to  display  all  open  locker  numbers  and  the  total  number of  open  lockers  when  the 
game ends. Hint: Use a list of 50 boolean elements, each of which indicates whether a locker is open 
(True) or closed (False)."""

# create 50 lockers, all closed (False)
lockers = [False] * 50

# players 1 to 50
for player in range(1, 51):

    #each player change locker that multiple f their numbber
    #i represent locker number from 1-50
    for i in range(player, 51, player):
        lockers[i-1] = not lockers[i-1]

#display open locker        
print (lockers)
for i in range(50):
    #if open true
    if lockers[i]:
        print(i+1,end=" ")

#total count locker are open
total_open = lockers.count(True)
print("Total open locker=" ,total_open)