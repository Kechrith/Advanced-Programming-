import random

suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King"]

deck = []
for suit in suits:
    for rank in ranks:
        deck.append((rank, suit))

# Shuffle deck
random.shuffle(deck)

def get_point(card):
    rank = card[0]
    if rank in ["Jack", "Queen", "King"]:
        return 0
    elif rank == "Ace":
        return 1
    else:
        return int(rank)

def calculate_points(cards):
    total = sum(get_point(card) for card in cards)
    return total % 10

user_cards = []
computer_cards = []

user_cards.append(deck.pop(0))
computer_cards.append(deck.pop(0))
user_cards.append(deck.pop(0))
computer_cards.append(deck.pop(0))

user_points = calculate_points(user_cards)
computer_points = calculate_points(computer_cards)

print("Your cards:", user_cards)
print("Your points:", user_points)

if user_points in [8, 9] or computer_points in [8, 9]:
    print("\nBoom!!!")
else:
    choice = input("Draw third card? (y/n): ")

    if choice.lower() == "y":
        user_cards.append(deck.pop())   # from bottom
        user_points = calculate_points(user_cards)
        print("Your new cards:", user_cards)
        print("Your new points:", user_points)

    draw = False
    number = random.randint(0, 99)

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

    if draw:
        computer_cards.append(deck.pop())
        computer_points = calculate_points(computer_cards)

print("\n----- Final Result -----")
print("Your cards:", user_cards)
print("Your points:", user_points)

print("Computer cards:", computer_cards)
print("Computer points:", computer_points)

if user_points > computer_points:
    print("Result: You Win!")
elif user_points < computer_points:
    print("Result: You Lose!")
else:
    print("Result: Draw!")
