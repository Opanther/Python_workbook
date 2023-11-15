# Store the admission price as constants
baby_price = 0.00
child_price = 14.00
adult_price = 23.00
senior_price = 18.00
# Store the age limit as constants
baby_limit = 2
child_limit = 12
adult_limit = 64

# Create a variable to hold the total admission cost for all guests
total = 0
# keep on reading ages until the user enters a blank line
line = input("Enter the age of the guest (blank to finish): ")
while line != "":
    age = int(line)
    if age <= baby_limit:
        total = baby_price
    elif age <= child_limit:
        total += child_price
    elif age <= adult_limit:
        total += adult_price
    else:
        total += senior_price
    # read the next age from the user
    line = input("Enter the age of the guest (Blank to finish): ")

# Display the total due for the group, formated using two decimal places
print(f"The total for that group is {total:.2f}")
