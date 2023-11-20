import random


def simulate_coin_flip():
    outcomes = []  # To store the outcomes of each simulation
    consecutive_count = 0  # Counter for consecutive heads or tails
    flips_count = 0  # Counter for total flips

    while consecutive_count < 3:
        # Simulate a coin flip (0 for heads, 1 for tails)
        outcome = random.randint(0, 1)

        # Display H for heads, T for tails
        print('H' if outcome == 0 else 'T', end=' ')

        # Check for consecutive heads or tails
        if not outcomes or outcomes[-1] == outcome:
            consecutive_count += 1
        else:
            consecutive_count = 1

        # Update outcomes and flips count
        outcomes.append(outcome)
        flips_count += 1

    print()  # Move to the next line after one simulation
    return flips_count


def main():
    total_flips = 0

    # Perform the simulation 10 times
    for _ in range(10):
        print("Simulation {}: ".format(_ + 1), end='')
        flips = simulate_coin_flip()
        total_flips += flips
        print("Number of flips: {}".format(flips))

    # Calculate and display the average number of flips
    average_flips = total_flips / 10
    print("\nAverage number of flips over 10 simulations: {:.2f}".format(average_flips))


if __name__ == "__main__":
    main()
