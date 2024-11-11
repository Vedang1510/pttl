# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

def hourglass_pattern(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(2, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

n = int(input("Enter the number of rows for the hourglass pattern: "))
hourglass_pattern(n)
