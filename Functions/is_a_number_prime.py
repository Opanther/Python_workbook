def isitprime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        return True


def main():
    num: int = int(input("Enter the number to check if it is a prime: "))
    if isitprime(num):
        print(" This number",num ," is a prime number")
    else:
        print(" This number",num ," is not a prime number")


if __name__ == "__main__":
    main()
