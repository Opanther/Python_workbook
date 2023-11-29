


## Improve the capitalization of a string
def capitalize_it(s):
    #create a copy of the string
    result = s
    # Capitalize the first non-space character in the string
    pos = 0
    while pos < len(s) and result[pos] == ' ':
        pos += 1
    if pos < len(s):
        #Replace the character with its uppercase version without changing any other characters
        result = result[0:pos] + result[pos].upper() + result[pos + 1: len(result)]
    # Capitalize the first letter that follows a ".","!' or "?"
    pos = 0
    while pos < len(s):
        if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
            #move past the '.','!' or '?'
            pos = pos + 1
            # move past any spaces
            while pos < len(s) and result[pos] == " ":
                pos = pos + 1
            # if we haven't reached the end of the string then replace the current character with its uppercase equivalent
            if pos < len(s):
                result = result[0 : pos] + result[pos].upper() + result[pos + 1 : len(result)]
        #move to the next character
        pos = pos + 1
    # Capitalize i when it is preceded by a space and followed by a space, period, excalmation mark, question mark or apostrophe
    pos = 1
    while pos < len(s) - 1:
        if result[pos -1 ] == " " and result[pos] == "i" and (result[pos - 1] == " " or result[pos + 1] == "." or result[pos + 1 ] == "!" or result[pos + 1] == "?" or result[pos +1] == "'" ):
        # replace the i with an I without changing any other characters
            result = result[0 : pos] + "I" + result[pos + 1 : len(result)]
        pos = pos + 1
    return result

def main():
    s = input("Enter the string to capitalize: ")
    capitalized = capitalize_it(s)
    print("it is capitalized as:", capitalized)


if __name__ == "__main__":
    main()
