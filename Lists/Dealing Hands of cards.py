from shuffling_a_deck_of_cards import createdeck, shuffle
from random import randrange

#
# def deal(hands, cards_per_hands, cards):
#     deals = [[cards for _ in range(cards)] for _ in range(hands)]
#     print(deals)
def deal(hands, cards_per_hand, cards):
    deals = [[cards[i * cards_per_hand + j] for j in range(cards_per_hand)] for i in range(hands)]
    print(deals)


def main():
    cards = createdeck()
    cards = shuffle(cards)
    deal(4, 5, cards)


if __name__ == "__main__":
    main()
