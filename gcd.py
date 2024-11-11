def find_gcd():
    # Taking two numbers as input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Using the Euclidean algorithm to find the GCD
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    # The GCD is stored in num1 after the loop ends
    print(f"The GCD is {num1}.")

find_gcd()
