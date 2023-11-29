def valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a valid triangle"
    elif a >= b + c or b >= a + c or c >= b + a:
        return "Not a valid triangle"
    else:
        return "Valid Triangle"

def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    result = valid_triangle(a, b, c)
    print("The result is", result)

if __name__ == "__main__":
    main()