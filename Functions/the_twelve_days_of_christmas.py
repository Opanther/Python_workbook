# def verse(day):
#     """Create a verse"""
#
#     ordinal = [
#         'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
#         'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
#     ]
#
#     gifts = [
#         'A partridge in a pear tree.',
#         'Two turtle doves,',
#         'Three French hens,',
#         'Four calling birds,',
#         'Five gold rings,',
#         'Six geese a laying,',
#         'Seven swans a swimming,',
#         'Eight maids a milking,',
#         'Nine ladies dancing,',
#         'Ten lords a leaping,',
#         'Eleven pipers piping,',
#         'Twelve drummers drumming,',
#     ]
#
#     lines = [
#         f'On the {ordinal[day - 1]} day of Christmas,',
#         'My true love gave to me,'
#     ]
#
#     lines.extend(reversed(gifts[:day]))
#
#     if day > 1:
#         lines[-1] = 'And ' + lines[-1].lower()
#
#     return '\n'.join(lines)
#
# def main():
#     day = int(input("Enter the day number "))
#     print("the verse of the day ", verse(day))
#
# if __name__ == "__main__":
#     main()

# solution 2
from Convert_an_integer_to_its_ordinal_number import cardinal2ordinal
def displayVerse(n):
    print("On the", cardinal2ordinal(n), "day of Christmas")
    print("my true love sent to me")

    if n>= 12:
        print("twelve drummers drumming")
    if n >= 11:
        print("Elven pipers piping,")
    if n >= 10:
        print("Ten lords a-leaping,")
    if n >= 9:
        print("Nine ladies dancing")
    if n >= 8:
        print("Eight maids a-milking,")
    if n >= 7:
        print("Seven swans a-swimming,")
    if n >= 6:
        print("Six geese a-laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two turtle doves")
    if n == 1:
        print("A", end=" ")
    else:
        print("And a", end= " ")
    print("partridge in a pear tree.")
    print()

def main():
    for verse in range(1, 13):
        displayVerse(verse)

main()
