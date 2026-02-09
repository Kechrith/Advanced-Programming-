'''
Group 9
Exercise2:
Write a function called display_longest_word that will accept a string, then displays the longest
word within the string.
'''

def display_longest_word(text):
    # Split the input text into words using whitespace as delimiter.
    words = text.split()

    # assume first word is the longest
    longest = words[0]

    # Iterate through each word and update 'longest' when a longer word is found.
    for word in words:
        if len(word) > len(longest):
            longest = word

    # Output the result to the user.
    print("The longest word is:", longest)

# Read a sentence from the user and call the function to display the longest word.
sentence = input("Enter a sentence: ")
display_longest_word(sentence)
