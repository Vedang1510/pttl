def categorize_numbers():
    # Taking input from the user
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    
    even_numbers = []
    odd_numbers = []
    
    # Categorizing numbers into even and odd
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    # Displaying the results
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)

categorize_numbers()
