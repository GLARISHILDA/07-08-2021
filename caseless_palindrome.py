# Write a function that checks if a given word is a palindrome. Character case should be ignored.
def is_palindrome(word): # function name

# Ignore Character case
    word = word.casefold()

# Reverse the string
    rev_word = reversed(word)

# check if the word is equal to its reverse
    if list(word) == list(rev_word):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

is_palindrome("RACEcar") # Calling the function name