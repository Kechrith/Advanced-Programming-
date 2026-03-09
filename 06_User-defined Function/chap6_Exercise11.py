"""
Group 9 
Write a program to simulate two players (user and computer) playing 
a card game (ដុកឌាំង / ប៉ក់) using a standard 52-card deck.
"""

import random 

# Define the four suits in a deck
suits = ["Diamonds", "Clubs", "Hearts", "Spades"]

# Define the ranks in a deck
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King"]

# Create a full deck of 52 cards using nested loops
deck = []
for suit in suits:
    for rank in ranks:
        deck.append((rank, suit))   # Each card is stored as (rank, suit)

# Shuffle the deck randomly
random.shuffle(deck)

# Function to get the point value of a single card
def get_point(card):
    rank = card[0]   # Get rank from card tuple
    
    # Face cards are worth 0 points
    if rank in ["Jack", "Queen", "King"]:
        return 0
    
    # Ace is worth 1 point
    elif rank == "Ace":
        return 1
    
    # Number cards keep their numeric value
    else:
        return int(rank)

# Function to calculate total points of cards (mod 10 rule)
def calculate_points(cards):
    total = sum(get_point(card) for card in cards)  # Sum all card points
    return total % 10   # Only keep last digit (rule of Dok Dang / Pok)

# Lists to store user and computer cards
user_cards = []
computer_cards = []

# Deal first two cards to both players
user_cards.append(deck.pop(0))
computer_cards.append(deck.pop(0))
user_cards.append(deck.pop(0))
computer_cards.append(deck.pop(0))

# Calculate initial points
user_points = calculate_points(user_cards)
computer_points = calculate_points(computer_cards)

# Show user's cards and points
print("Your cards:", user_cards)
print("Your points:", user_points)

# Check for natural 8 or 9 (Boom)
if user_points in [8, 9] or computer_points in [8, 9]:
    print("\nBoom!!!")   # Automatic stop if natural win
else:
    # Ask user if they want to draw a third card
    choice = input("Draw third card? (y/n): ")

    if choice.lower() == "y":
        user_cards.append(deck.pop())   # Draw card from deck
        user_points = calculate_points(user_cards)
        print("Your new cards:", user_cards)
        print("Your new points:", user_points)

    # Computer decision logic
    draw = False
    number = random.randint(0, 99)   # Random number for probability

    # Computer drawing rules (probability-based)
    if computer_points < 4:
        draw = True
    elif computer_points == 4 and number < 80:
        draw = True
    elif computer_points == 5 and number < 40:
        draw = True
    elif computer_points == 6 and number < 10:
        draw = True
    elif computer_points >= 7:
        draw = False

    # If computer decides to draw
    if draw:
        computer_cards.append(deck.pop())
        computer_points = calculate_points(computer_cards)

# Show final results
print("\n----- Final Result -----")
print("Your cards:", user_cards)
print("Your points:", user_points)

print("Computer cards:", computer_cards)
print("Computer points:", computer_points)

# Compare scores and print result
if user_points > computer_points:
    print("Result: You Win!")
elif user_points < computer_points:
    print("Result: You Lose!")
else:
    print("Result: Draw!")