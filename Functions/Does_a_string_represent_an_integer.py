def isInteger(string):
    s_s = string.strip()
    if (s_s[0] == "+" or s_s[0] == "-") and s_s[1:].isdigit():
        return True
    if s_s.isdigit():
        return True

    return False


def main():
    string = input("Enter the input to check for a string :")
    if isInteger(string):
        print("That string represents an integer.")
    else:
        print(" That string does not represent an integer.")


if __name__ == "__main__":
    main()
