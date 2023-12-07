list = []

def format_list(items):

    length = len(items)

    if length == 0:
        return 'Empty'
    elif length == 1:
        return str(items[0])

    results = ''
    for i in range(0, length - 2):
        results += str(items[i]) + ", "

    results = results + str(items[length - 2]) + ' and '
    results += str(items[length - 1])

    return results

def main():
    items = []
    line = input('Enter an item (Enter to cancel): ')
    while line != '':
        items.append(line)
        line = input('Enter an item (Enter to cancel): ')

    print('The items you entered are: {}'.format(format_list(items)))


if __name__ == "__main__":
    main()