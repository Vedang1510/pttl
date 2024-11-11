def find_minimum():
    # Taking three numbers as input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    # Finding the minimum of the three numbers
    minimum = min(num1, num2, num3)
    
    # Displaying the result
    print(f"The minimum of {num1}, {num2}, and {num3} is {minimum}.")

find_minimum()
