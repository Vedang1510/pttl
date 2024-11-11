def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number to calculate its factorial: "))
print(f"Factorial of {n} is:", factorial_iterative(n))
