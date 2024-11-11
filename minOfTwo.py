def find_minimum_two():
    # Taking two numbers as input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Finding the minimum of the two numbers
    minimum = min(num1, num2)
    
    # Displaying the result
    print(f"The minimum of {num1} and {num2} is {minimum}.")

find_minimum_two()
