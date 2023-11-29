import random


def old_license_plate():
    password_length = 6
    result = ""
    for i in range(password_length):
        if i < 3:
            randomchar = chr(random.randint(97, 122))
            result += randomchar
        else:
            randomnumber = chr(random.randint(48, 57))
            result += randomnumber
    return result


def new_license_plate():
    password_length = 7
    result = ""
    for i in range(password_length):
        if i < 4:
            randomnumber = chr(random.randint(48, 57))
            result += randomnumber
        else:
            randomchar = chr(random.randint(97, 122))
            result += randomchar
    return result

def main():
    print(new_license_plate(), old_license_plate())

if __name__ == "__main__":
    main()
