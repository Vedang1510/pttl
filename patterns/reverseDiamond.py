# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******

def reverse_diamond_pattern(n):
    for i in range(n - 1, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(1, n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

n = int(input("Enter the number of rows for the reverse diamond pattern: "))
reverse_diamond_pattern(n)
