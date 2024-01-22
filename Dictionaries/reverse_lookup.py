# Conduct a reveser lookup on a dictionary, finding all the keys that map to the provided value
def reverse_lookup(data, value):
    # construct a list of the keys that map to value
    keys = []
    # check each key and add it to keys if the values match
    for key in data:
        if data[key] == value:
            keys.append(key)

    return keys


# demonstrate the reverselookup function
def main() -> object:
    # A dictionary mapping four french words to their english equivalents
    fren = {"le": "the", "la": "the", "livre": "book", "pomme": "apple"}

    # Demonstarte the reverse lookup function with 3 cases: One that returns multiple keys, one that return one keys and one that return no key s
    print("The french words for 'the' are: ", reverse_lookup(fren, "the"))
    print("expected: ['le', 'la']")
    print()
    print("The French word for apple is", reverse_lookup(fren, 'apple'))
    print("expected: ['pomme']")
    print()
    print("The French word for asdf is", reverse_lookup(fren, 'asdf'))
    print("expected: []")
    print()

if __name__ == "__main__":
    main()



