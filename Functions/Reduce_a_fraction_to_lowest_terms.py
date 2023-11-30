def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def to_lowest_terms_fraction(n, m):
    gcd = find_gcd(n, m)

    numerator = n // gcd
    denominator = m // gcd

    return numerator, denominator

def main():
    n = int(input("Enter the first number: "))
    m = int(input("Enter the second number: "))

    if n < 0 or m <= 0:
        print("Please enter valid positive integers.")
        return

    numerator, denominator = to_lowest_terms_fraction(n, m)

    print(f"The fraction {n}/{m} in lowest terms is: {numerator}/{denominator}")

if __name__ == "__main__":
    main()


