pennies_per_nickel = 5
Nickel = 0.05
# track the total cost for all the items
total = 0.00
# Read the price of the first item as a string
line = input("Enter the price of the item (blank to quit):")
# Continue reading items until a blank line is entered
while line != "":
    # add the total cost of the item to the total (after converting it to a floating-point number)
    total = total + float(line)

    # read the cost of the next item
    line = input("Enter the price of the item (blank to quit):")
# display the exact total payable
print(f"The exact amount payable is {total:.2f}")

# compute the number of pennies that would be left if the total was paid using nickels
rounding_indicator = total * 100 % pennies_per_nickel

if rounding_indicator < pennies_per_nickel / 2:
    # if the number of pennies left is less than 2.5 then we round down by subtracting that number of pennies from
    # the total
    cash_total = total - rounding_indicator / 100
else:
    # otherwise we add a nickel and then subtract the number of pennies
    cash_total = total + Nickel - rounding_indicator / 100
# display amount due when paying with cash
print(f"The cash amount payable is {cash_total:.2f}")
