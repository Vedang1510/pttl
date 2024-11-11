#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

def number_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + (str(i) + " ") * i)

n = int(input("Enter the number of rows for the number pyramid: "))
number_pyramid(n)
