
# Step 1: Create empty lists to store numbers
positive = []
negative = []
zero = []

# Step 2: Use a loop to repeatedly get numbers from the user
while True:
    # Step 3: Prompt the user to enter a number
    try:
        number = float(input("Enter a number (enter a non-number to quit): "))
    except ValueError:
        # If the user enters a non-number, break out of the loop
        break

    # Step 4: Categorize the number
    if number < 0:
        negative.append(number)
    elif number == 0:
        zero.append(number)
    elif number > 0:
        positive.append(number)

# Step 5: Display the categorized numbers entered by the user
print("Negative Numbers:")
for i in negative:
    print(i)

print("Zeroes:")
for i in zero:
    print(i)

print("Positive Numbers:")
for i in positive:
    print(i)
