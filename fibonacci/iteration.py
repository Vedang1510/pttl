def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence[:n]

n = int(input("Enter the number of terms for the Fibonacci series: "))
print("Fibonacci Series:", fibonacci_iterative(n))
