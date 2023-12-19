from random import randrange


def createdeck():
    """
    Creates a complete deck of 52 cards.

Returns:
    list: A list containing all 52 cards in the standard deck.
    """
    value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "k", "A"]
    suits = ["s", "h", "d", "c"]

    deck = [f"{r} in {s}" for r in value for s in suits]

    return deck


def shuffle(deck):
    """Fisher-Yates Shuffle"""
    for i in range(0, len(deck)):
        other_pos = randrange(i, len(deck))
        temp = deck[i]
        deck[i] = deck[other_pos]
        deck[other_pos] = temp
        return deck


# Optimizing the shuffle code The current implementation of the Fisher-Yates shuffle uses two nested loops,
# which can be inefficient for large decks. A more efficient approach involves modifying the seed of the random
# number generator after each swap. This way, the random positions generated will be less predictable, leading to a
# more thorough shuffling.

# def shuffle(deck):
#     rng = random.Random()
#     for i in range(len(deck) - 1, -1, -1):
#         other_pos = rng.randrange(i + 1)
#         deck[i], deck[other_pos] = deck[other_pos], deck[i]

def main():
    cards = createdeck()
    print("The original deck of cards is: ")
    print(cards)
    print()

    shuffle(cards)
    print("The shuffled deck of cards is: ")
    print(cards)


if __name__ == "__main__":
    main()
