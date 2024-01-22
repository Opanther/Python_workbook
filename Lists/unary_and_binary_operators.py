# Differentitate between unary and binary + and - operators

from Tokenizing_a_string import tokenlist

def identifyUnary(tokens):
    retval = []
    # process each tooken in the list
    for i in range(len(tokens)):
        # if the first token in the list is + or - then it is a unary operator
        if i == 0 and (tokens[i] == "+" or tokens[i] == "-"):
            retval.append("u" + tokens[i])
        # if the tokem is a + or - and the previous token is an operator or an open parenthesis then it is a unary operator
        elif i > 0 and ( tokens[i] == "+" or tokens[i] == "-") and (tokens[i-1] == "+" or tokens[i-1] == "-" or tokens[i-1] == "*" or tokens[i-1] == "/" or tokens[i-1] =="("):
            retval.append("u" + tokens[i])
        else:
            retval.append(tokens[i])

    return retval

def main():
    # read an expression from the user, tokenize it, and display the result
    exp = input("Enter a mathematical expression: ")
    tokens = tokenlist(exp)
    print("The tokens are:", tokens)
    # identify the unary operators in the list of tokens
    marked = identifyUnary(tokens)
    print("With unary operators marked: ", marked)


if __name__ == "__main__":
    main()

