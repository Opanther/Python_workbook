import random


def generate_pass():
    password_length = random.randint(7, 10)
    result = ""
    for i in range(password_length):
        randomchar = chr(random.randint(33, 126))
        result += randomchar
    return result


def main():
    print("your random password is: ", generate_pass())


if __name__ == "__main__":
    main()
