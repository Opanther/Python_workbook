import math

# Number of approximations to display
num_approximations = 15

# Initialize the value of pi and the denominator for the series
pi_approx = 0
denominator = 1

for i in range(num_approximations):
    # Calculate the current approximation using the Leibniz formula
    pi_approx += 4 / denominator if i % 2 == 0 else -4 / denominator
    denominator += 2

    # Display the current approximation
    print(f"Approximation {i + 1}: {pi_approx:.10f}")

# Compare the final approximation with the math library's pi value
print(f"Math library value of π: {math.pi:.10f}")