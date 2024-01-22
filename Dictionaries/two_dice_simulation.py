import random
#Step 1: Dice roll simulation function
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)
# Calculate the theoretical Probabilities: number of ways to achieve each total and then compute the probability
def theoretical_probability(total):
    count = 0
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            if die1 + die2 == total:
                count += 1
    return (count / 36) * 100

def main():
    #rolling the dice 1000 times and counting totals
    roll_counts = {total: 0 for total in range(2, 13)}
    for _ in range(1000):
        total = roll_dice()
        roll_counts[total] += 1

    print("Total", "Count", "Experimental %", "Theoretical %", sep='\t')
    for total in range(2, 13):
        experimental_percentage = (roll_counts[total] / 1000) * 100
        theoretical_percentage = theoretical_probability(total)
        print(f"{total}\t{roll_counts[total]}\t{experimental_percentage:.2f}%\t{theoretical_percentage:.2f}%")

if __name__ == "__main__":
    main()
