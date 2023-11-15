# Revisit this structure for my code when doing the function Chapter

def newton_sqrt(x, epsilon=1e-12):
        guess = x / 2  # Initial guess, you can choose any reasonable value
        while abs(guess * guess - x) > epsilon:
            guess = (guess + x / guess) / 2
        return guess


try:
        x = float(input("Enter a number: "))
        if x < 0:
            print("Sorry, the square root of a negative number is not defined.")
        else:
            sqrt = newton_sqrt(x)
            print(f"The square root of {x} is approximately {sqrt:.6f}")
except ValueError:
        print("Invalid input. Please enter a valid number.")