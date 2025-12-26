"""
Group9
# Write the program to create a dictionary from user input
"""

# Initialize an empty dictionary
my_dictionary = {}

# Ask user for input
print("Enter key and value separated by a comma : ")
print("Type 'done' when you are finished. ")

# Loop to get user input
while True:
    user_input = input("Enter key value: ")

    # Check if user wants to stop
    if user_input.lower() == "done":
        break

    # Check if input has a comma
    if "," not in user_input:
        print("Please use a comma between key and value.")
        continue

    # Split into key and value
    key, value = user_input.split(",")
    key = key.strip()
    value = value.strip()

    # Add to dictionary
    my_dictionary[key] = value

# Display the resulting dictionary
print("Your dictionary is:")
print(my_dictionary)