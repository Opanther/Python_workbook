# def drawbox():
#     print("**********")
#     print("*        *")
#     print("*        *")
#     print("**********")
#
# drawbox()
# Draw a box outlined with asterisks and filled with spaces.
# @param width the width of the box
# @param height the height of the box


# def drawbox(width, height):
#     # A Box that is smaller than 2x2 cannot be drawn with this function
#     if width < 2 or height < 2:
#         print("Error: The width or height is too small.")
#         quit()
#     # Draw the top of the box
#     print("*" * width)
#
#     # Draw the side of the box
#     for i in range(height - 2):
#         print("*" + " " * (width - 2) + "*")
# #
# #     #Draw the top of the box
# #     print("*" * width)
#
#
# def drawbox(width, height, outline="*", fill=" "):
#     # A Box that is smaller than 2x2 cannot be drawn with this function
#     if width < 2 or height < 2:
#         print("Error: The width or height is too small.")
#         quit()
#     # Draw the top of the box
#     print(outline * width)
#
#     # Draw the side of the box
#     for i in range(height - 2):
#         print(outline + fill * (width - 2) + outline)
#
#     # Draw the top of the box
#     print(outline * width)
#
#
# drawbox(14, 5, "@", ".")
#
#
# def sumGeometric(a, r, n):
#     if r == 1:
#         return a * n
#     s = a * (1 - r ** n) / (1 - r)
#     return s
#
#
# def main():
#     # Read the initial value for the first sequence
#     init = float(input("Enter the value of a (0 to quitt) :"))
#     while init != 0:
#         ratio = float(input("Enter the ratio, r: "))
#         num = int(input("Enter the number of terms, n :"))
#
#         # Compute and display the total
#         total = sumGeometric(init, ratio, num)
#         print("The sum of the first", num, "term is ", total)
#
#         # read the initial value for the next sequence
#         init = float(input("Enter the value of a (0 to quitt) :"))
#
#
# if __name__ == "__main__":
#     main()


from math import sqrt

def hypotenuse(a, b):
    c = sqrt(a**2 + b**2)
    return c

def main():
    a = int(input("Enter the length of the side a:"))
    b = int(input("Enter the length of the side b:"))
    total= hypotenuse(a, b)
    print("The length of the hypotenuse is", total)




if __name__ == "__main__":
    main()