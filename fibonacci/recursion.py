def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter the number of terms for the Fibonacci series: "))
fib_series = [fibonacci_recursive(i) for i in range(n)]
print("Fibonacci Series:", fib_series)
