# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1

def inverted_number_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + (str(i) + " ") * i)

n = int(input("Enter the number of rows for the inverted number pyramid: "))
inverted_number_pyramid(n)
