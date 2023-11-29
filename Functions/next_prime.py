from is_a_number_prime import isitprime

def nextPrime(n):
    m = n + 1
    while True:
        if isitprime(m):
            return m
        m += 1

def main():
    m_value = int(input("Enter a value for m: "))
    result = nextPrime(m_value)
    print(f"The next prime number larger than {m_value} is: {result}")


if __name__ == "__main__":
    main()
