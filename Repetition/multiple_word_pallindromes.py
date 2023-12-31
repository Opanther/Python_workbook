

# Read the string from the user
sentence = input("Check if a sentence is a Palindrome: ")

# Remove spaces and convert to lowercase
sentence = sentence.replace(" ", "").lower()

# Assume that it is a palindrome until we can prove otherwise
is_palindrome = True

# Check the characters, starting from the beginning and end. Continue until the middle is reached or we have determined that the string is not a palindrome.
i = 0
while i < len(sentence) / 2 and is_palindrome:
    # If the characters do not match, mark that the sentence is not a palindrome
    if sentence[i] != sentence[len(sentence) - i - 1]:
        is_palindrome = False
    # Move to the next character
    i += 1

# Display a meaningful output message
if is_palindrome:
    print("The sentence is a palindrome")
else:
    print("The sentence is not a palindrome")
