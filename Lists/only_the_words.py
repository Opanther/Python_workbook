
# Define a function to extract only the words from a sentence and remove specified punctuation characters
def onlythewords(s):
    # Step 1: Define a string of punctuation characters to be removed, used triple-quoted strings or escape sequences for multiline strings
    punctuations = ''',., ?- '!:;'''

    # Step 2: Split the input sentence into a list of words
    words = s.split()

    # Step 3: Iterate through each word in the list
    for i in words:
        # Step 4: Iterate through each character in the word
        for j in i:
            # Step 5: Check if the character is a punctuation character
            if j in punctuations:
                # Step 6: If true, remove the punctuation character from the word
                i = i.replace(j, '')

    # Step 7: Return the list of words (although some may still contain punctuation)
    return words


# Define the main function to get user input and display the result
def main():
    # Step 8: Prompt the user to enter a sentence
    sentence = input("Enter a sentence: ")

    # Step 9: Call the onlythewords function to extract words and remove punctuation
    result = onlythewords(sentence)

    # Step 10: Display the result
    print("The only words for", sentence, "are", result)


# Step 11: Check if the script is being run as the main program
if __name__ == "__main__":
    # Step 12: If true, call the main function
    main()
