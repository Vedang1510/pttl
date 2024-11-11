# 10 9 8 7
#  6 5 4
#   3 2
#    1

def reverse_floyds_triangle(n):
    num = n * (n + 1) // 2
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        for j in range(i):
            print(num, end=" ")
            num -= 1
        print()

n = int(input("Enter the number of rows for Reverse Floyd’s Triangle: "))
reverse_floyds_triangle(n)
