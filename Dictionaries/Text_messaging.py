# Create a dictionary that maps each letter or symbol to the key presses needed
key_mapping = {
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
    ' ': '0',
    ',': '1', '.': '11', '?': '111', '!': '1111', ':': '11111'
}

# Function to convert a message to key presses
def message_to_key_presses(message):
    key_presses = ''
    for char in message:
        if char.upper() in key_mapping:
            key_presses += key_mapping[char.upper()]
    return key_presses

# Get user input and convert it to key presses
user_input = input("Enter a message: ")
key_presses_result = message_to_key_presses(user_input)

# Display the key presses needed for the user's message
print(key_presses_result)
