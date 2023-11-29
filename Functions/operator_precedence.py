
def precedence(s):
    if "+" in s or "-" in s:
        return 1
    elif "*" in s or "/" in s:
        return 2
    elif "^" in s:
        return 3
    else:
        return -1

def main():
    s = input("Enter the string to check the operator precedence:")

    if precedence(s) == -1:
        print("That string does not have an operator.")
    else:
        print(f"The operator precedence of '{s}' is {precedence(s)}.")

if __name__ == "__main__":
    main()

