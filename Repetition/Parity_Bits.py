
# Continue looping until a blank line is entered
while True:
    # Read the first line of input
    line = input("Enter a string containing 8 bits (leave blank to finish):")

    # Check if the line is blank
    if line == "":
        break

    # Ensure that the line has a total of 8 zeros and ones and exactly 8 characters
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        # Display an appropriate error message
        print("That wasn't 8 bits. Try again.")
    else:
        # Count the number of ones
        ones = line.count("1")

        # Display the parity bit
        if ones % 2 == 0:
            print("The parity bit should be 0.")
        else:
            print("The parity bit should be 1.")
