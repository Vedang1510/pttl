# *****
#  ****
#   ***
#    **
#     *
#    **
#   ***
#  ****
# *****

def sandglass_pattern(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)
    for i in range(2, n + 1):
        print(" " * (n - i) + "*" * i)

n = int(input("Enter the number of rows for the sandglass pattern: "))
sandglass_pattern(n)
