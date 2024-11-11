# 1
# 2 3
# 4 5 6
# 7 8 9 10

def floyds_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

n = int(input("Enter the number of rows for Floyd’s Triangle: "))
floyds_triangle(n)
