# *
# **
# ***
# ****
# *****

def right_angle_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

n = int(input("Enter the number of rows for the right-angle triangle: "))
right_angle_triangle(n)
