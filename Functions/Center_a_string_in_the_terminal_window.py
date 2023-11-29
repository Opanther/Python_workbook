# Center a string of characters within a certain width
width = 80

## Create a new string that will be centered within a given width when it is printed.
#  @ param s the string that will be centered
#  @ param width the width in which the string will be centered
#  @ return a new copy of s that contains the leading spaces needed to center s
def center(s, width):
    # if the string is too long to center, then the original string is returned
    if width < len(s):
        return s
    # computes the number of spaces needed and generate the result
    spaces = (width - len(s)) // 2
    result = " " * spaces + s

    return result

def main():
    print(center("A Famous Story", width))
    print(center("by:", width))
    print(center("Tomi Oredein", width))
    print()
    print("Once upon a time...")


if __name__ == "__main__":
    main()
