# A program asks to check whether two words are anagrams or not
def is_anagram(s1, s2):
    # Remove spaces and convert to lowercase (optional but useful)
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Sort letters and compare
    return sorted(s1) == sorted(s2)


# Example test
print(is_anagram("binary", "brainy"))  # True
print(is_anagram("hello", "world"))    # False
