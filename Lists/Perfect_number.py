# Import the properdivisor function from the module list_of_proper_divisors.py
from list_of_proper_divisors import properdivisor

# Define the limit for finding perfect numbers
limit = 10000

# Define a function to check if a number is a perfect number
def perfectnumber(n):
    # Step 1: Find the proper divisors of the number using the properdivisor function
    divisor = properdivisor(n)

    # Step 2: Calculate the sum of the proper divisors
    total = 0
    for d in divisor:
        total += d

    # Step 3: Check if the sum of proper divisors is equal to the number
    if total == n:
        # Step 4: If true, the number is a perfect number
        return True
    else:
        # Step 5: If false, the number is not a perfect number
        return False

# Define the main function to find and print perfect numbers within the specified limit
def main():
    # Step 6: Print a message indicating the range of numbers being considered
    print("The perfect numbers between 1 and", limit, "are:")

    # Step 7: Iterate through numbers from 1 to the specified limit
    for i in range(1, limit + 1):
        # Step 8: Check if the current number is a perfect number using the perfectnumber function
        if perfectnumber(i):
            # Step 9: If true, print the perfect number
            print("", i)

# Step 10: Check if the script is being run as the main program
if __name__ == "__main__":
    # Step 11: If true, call the main function
    main()


