#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1

def pascals_triangle(n):
    for i in range(n):
        print(" " * (n - i), end="")
        value = 1
        for j in range(i + 1):
            print(value, end=" ")
            value = value * (i - j) // (j + 1)
        print()

n = int(input("Enter the number of rows for Pascal’s Triangle: "))
pascals_triangle(n)
