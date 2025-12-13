"""Ask the user to enter their favorite color. If they enter “red”, “RED” or “Red” display the message “I 
like red too”, otherwise display the message “I don’t like [color], I prefer red”."""

# # Ask the user to enter their favorite color
color = input("Enter your Favorite color: ")

# If the color is red
if color.lower() == "red":
    print("I like red too ")

# If the color is not red, display this message including the user's color
else: 
    print("I dont like", color, "I prefer")