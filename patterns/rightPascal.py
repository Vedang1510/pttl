# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def right_pascals_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)
    for i in range(n - 1, 0, -1):
        print("*" * i)

n = int(input("Enter the number of rows for Right Pascal’s Triangle: "))
right_pascals_triangle(n)
