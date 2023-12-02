# Step 1: Create an empty list to store words
words = []

# Step 2: Prompt the user to enter a word
word = input("Enter a word (blank line to quit): ")

# Step 3: Use a loop to repeatedly get words from the user until a blank line is entered
while word != "":
    # Step 4: Check if the word is not already in the list
    if word not in words:
        # Step 5: If the word is not a duplicate, add it to the list
        words.append(word)

    # Step 6: Prompt the user to enter another word
    word = input("Enter a word (blank line to quit): ")

# Step 7: Display the unique words entered by the user
for word in words:
    print(word)

