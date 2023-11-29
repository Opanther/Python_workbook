# Old code but it's not correct because it urrent implementation will return True as soon as it finds
# any uppercase letter, lowercase letter, or numeric character in the password. This means that it only checks the
# first character of the password for each of these conditions and returns immediately. As a result, the check for
# a password length of at least 8 characters is not being effectively enforced.


# def password_checker(p):
#     if len(p) >= 8:
#         return True
#     for i in p:
#         if i.isupper():
#             return True
#         if i.islower():
#             return True
#         if i.isnumeric():
#             return True
#     return False
#
#
# def main():
#     p = input("Enter password to check, if it's good :")
#     if password_checker(p):
#         print("That is a good password.")
#     else:
#         print("That isn't a good password")
#
#
# if __name__ == "__main__":
#     main()

def password_checker(p):
    # Check the length first
    if len(p) < 8:
        return False

    # Check for at least one uppercase letter, lowercase letter, and numeric character
    has_uppercase = False
    has_lowercase = False
    has_numeric = False

    for i in p:
        if i.isupper():
            has_uppercase = True
        elif i.islower():
            has_lowercase = True
        elif i.isnumeric():
            has_numeric = True

    # Return True only if all conditions are met
    return has_uppercase and has_lowercase and has_numeric


def main():
    p = input("Enter password to check if it's good: ")
    if password_checker(p):
        print("That is a good password.")
    else:
        print("That isn't a good password.")


if __name__ == "__main__":
    main()
