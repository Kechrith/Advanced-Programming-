"""
(Anagram) Two words are anagrams if they contain the same letters in different orders, for example, 
binary and brainy. Write a method called is_anagram that takes two strings and returns True if they 
are anagrams, otherwise, returns False.
"""

def is_anagram(s1, s2):
    # Remove spaces and convert to lowercase (optional but useful)
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Sort letters and compare
    return sorted(s1) == sorted(s2)


# Example test
print(is_anagram("binary", "brainy"))  # True
print(is_anagram("hello", "world"))    # False
