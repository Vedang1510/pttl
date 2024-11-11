def check_prime():
    # Taking input from the user
    num = int(input("Enter a number to check if it is prime or non-prime: "))
    
    # Handling cases for numbers less than 2
    if num < 2:
        print(f"{num} is a non-prime number.")
        return
    
    # Checking if the number is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is a non-prime number.")
            return
    
    print(f"{num} is a prime number.")

check_prime()
