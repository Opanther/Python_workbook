# Define a function to find the proper divisors of a positive integer
def properdivisor(n):
    # Step 1: Initialize an empty list to store proper divisors
    divisor = []

    # Step 2: Iterate from 1 to n//2 (inclusive) to find proper divisors
    for i in range(1, n//2 + 1):
        # Step 3: Check if i is a proper divisor (divides evenly into n and is less than n)
        if n % i == 0 and i < n:
            # Step 4: If true, add i to the list of proper divisors
            divisor.append(i)

    # Step 5: Return the list of proper divisors
    return divisor


# Define the main function to get user input and display the result
def main():
    # Step 6: Prompt the user to enter a number to check
    number = int(input("Enter the number to check: "))

    # Step 7: Call the properdivisor function to find the proper divisors
    n_divisors = properdivisor(number)

    # Step 8: Display the result
    print("The number of proper divisors for", number, "is", n_divisors)


# Step 9: Check if the script is being run as the main program
if __name__ == "__main__":
    # Step 10: If true, call the main function
    main()
