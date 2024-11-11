#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *

def hollow_diamond(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*" * (i != 0))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*" * (i != 0))

n = int(input("Enter the number of rows for the hollow diamond: "))
hollow_diamond(n)
