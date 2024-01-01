# Tokenizew a string containing a mathematical expression
# Convert a mathematical expression into a list of tokens
def tokenlist(s):
    # remove all of the spaces from s
    s = s.replace(" ", "")
    token = []
    i = 0
    while i < len(s):
        # Handle the tokens that are always a single character: *,/,^,( and )
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or s[i] == "(" or s[i] == ")" or s[i] == "+" or s[i] == "-":
            token.append(s[i])
            i += 1
        # Handle a number without a leading + or -
        elif "0" <= s[i] <= "9":
            num = ""
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                num = num + s[i]
                i += 1
            token.append(num)
        # any other character means the expression is not valid, return an empty list to indicate an error occured
        else:
            return []
    return token


def main():
    exp = input("Enter a mathematical expression: ")
    token = tokenlist(exp)
    print("The tokens are: ", token)


if __name__ == "__main__":
    main()
