# Exercise 3: Open a file, display its content, and handle errors

try:
    # Try to open the file in read mode
    file = open("example.txt", "r")

    # Display the content of the file
    print(file.read())

# Handle the error if the file does not exist
except FileNotFoundError:
    print("File not found.")

# This block runs if the file is opened successfully
else:
    print("File read successfully!")

    # Close the file
    file.close()

# This block always runs
finally:
    print("Program Ended!")