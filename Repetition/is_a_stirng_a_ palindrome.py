#Read the string from the user
word = input("Check if a word is a Palindrome: ")

# Assume that is palindrome until we can prove otherwise
is_palindrome = True

# Check the character,starting from the end. Continue until middle is reached or we have determined that the string is not palindrome.
i = 0
while i < len(word) / 2 and  is_palindrome:
    # if the characters do not match then mark that the string is not a palindrome
    if word[i] != word[len(word) - i - 1]:
        is_palindrome = False
   #Move to the next character
    i += 1

# Display a meaninful output message
if is_palindrome:
    print(word, "is a palindrome(Ailihphilia)")
else:
    print(word, "is not a palindrome(Aibohphobia)")
