# *****
# ****
# ***
# **
# *


def inverted_right_angle_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)

n = int(input("Enter the number of rows for the inverted right-angle triangle: "))
inverted_right_angle_triangle(n)
