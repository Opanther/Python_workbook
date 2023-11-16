number_user = int((input("Enter an integer (2 or greater):")))
if number_user < 2:
    print("Error please write a number greater than 2")
else:
    factor = 2
    while factor <= number_user:
        if number_user % factor == 0:
            print(f"{factor} is a factor of {number_user} ")
            number_user = number_user // factor
        else:
            factor = factor + 1


