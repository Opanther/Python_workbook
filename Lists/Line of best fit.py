#
# x_values = []
# y_values = []
# n = 0
#
#
# while True:
#     x = input("Enter x coordinate (blank line to quit): ")
#     if x == "":
#         break
#
#     num = float(x)
#     x_values.append(num)
#     n += 1
#
#     y = input("Enter y coordinate (blank line to quit): ")
#     if y == "":
#         break
#
#     num_y = float(y)
#     y_values.append(num_y)
#
# if len(x_values) == len(y_values):
#     # Calculate the mean of x and y values
#     mean_x = sum(x_values) / n
#     mean_y = sum(y_values) / n
#
#     # Calculate sigma_xy, sigma_x2, and sigma_y
#     sigma_x = sum(x_values)
#     sigma_y = sum(y_values)
#     sigma_x2 = sigma_x ** 2
#     sum_x2 =  sum(x**2 for x in x_values)
#
#     # Calculate the slope (m) and intercept (b)
#     m = ((sigma_x * sigma_y) - (mean_x * mean_y / n)) / (sum_x2 - (sigma_x2/n))
#     b = mean_y - m * mean_x
#
#     # Print the equation of the line of best fit
#     print(f"The equation of the line of best fit is y = {m}x + {b}")
# else:
#     print("The lengths of the two lists are not equal.")

def calculate_line_of_best_fit(x_values, y_values):
    n = len(x_values)

    # Calculate the sums needed for the formulas
    sigma_x = sum(x_values)
    sigma_y = sum(y_values)
    sigma_xy = sum(xi * yi for xi, yi in zip(x_values, y_values))
    sigma_x_squared = sum(xi ** 2 for xi in x_values)

    # Calculate the coefficients of the line of best fit
    m = (n * sigma_xy - sigma_x * sigma_y) / (n * sigma_x_squared - sigma_x ** 2)
    b = (sigma_y - m * sigma_x) / n

    return m, b

def main():
    x_values = []
    y_values = []

    while True:
        x_input = input("Enter x coordinate (blank line to quit): ")
        if x_input == "":
            break

        y_input = input("Enter y coordinate: ")
        if y_input == "":
            break

        x_values.append(float(x_input))
        y_values.append(float(y_input))

    m, b = calculate_line_of_best_fit(x_values, y_values)

    print(f"The equation of the line of best fit is: y = {m}x + {b}")

if __name__ == "__main__":
    main()

