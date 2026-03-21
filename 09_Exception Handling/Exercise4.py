# Write a program that ask the user for a key and display corresponding value
# Create a dictionary with integer keys and string values
data = {
    1: "Apple",
    2: "Banana",
    3: "Orange"
}

try:
    # Ask the user to input a key
    key = int(input("Enter a key 1-3: "))   
    
    # Display the value corresponding to the key
    print("Value:", data[key])

# Handle error if the key is not in the dictionary
except KeyError:
    print("Key not found in the dictionary.")

# Handle error if the user enters something that is not an integer
except ValueError:
    print("Invalid input. Please enter an integer key.")