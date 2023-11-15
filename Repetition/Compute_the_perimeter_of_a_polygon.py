from math import sqrt

# store the perimeter of the polygon
perimeter = 0
# Read the coordinate of the first point
first_x = float(input("Enter the first x-coordinate: "))
first_y = float(input("Enter the first y-coordinate: "))

# provide the initial values for prev_x and prev_y
prev_x = first_x
prev_y = first_y

# Read the remaining coordinates
line: str = input("Enter the next x-coordinate (Blank to quit):")
while line != "":
    # Covert the x-coordinate to a number and read the y-coordinate
    x = float(line)
    y = float(input("Enter the next y-coordinate: "))
    # compute the distance to the previous point and add it to the perimeter
    dist = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    perimeter = perimeter + dist

    # Set up prev_x and prev_y for the next loop iteration
    prev_x = x
    prev_y = y

    # read the next x-coordinate
    line = input("Enter the next x-coordinate (blank to quit): ")
dist = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
perimeter = perimeter + dist

# display the result
print("The perimeter of that polygon is", perimeter)
