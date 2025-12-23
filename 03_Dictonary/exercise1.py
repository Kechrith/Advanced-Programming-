# Group 9
# Write a program to that allow the user to create a 1D dict.

# Create an empty dictionary
my_dict = {}

print("Create your dictionary by entering key-value pairs.")
print("Format: key,value")
print("Type 'done' when finished.")
print()

# Loop to get user input
while True:
    user_input = input("Enter key-value pair (or 'done' to finish): ")

    # Check if user wants to stop
    if user_input.lower() == 'done':
        break

    # Split the input by comma
    if ',' in user_input:
        parts = user_input.split(',', 1)  # Split only at first comma
        key = parts[0].strip()
        value = parts[1].strip()

        # Add to dictionary
        my_dict[key] = value
        print(f"Added: {key} -> {value}")
    else:
        print("Invalid format. Please use: key,value")

# Display the final dictionary
print("\nFinal Dictionary:")
print(my_dict)