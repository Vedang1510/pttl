def find_maximum():
    # Taking three numbers as input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    # Finding the maximum of the three numbers
    maximum = max(num1, num2, num3)
    
    # Displaying the result
    print(f"The maximum of {num1}, {num2}, and {num3} is {maximum}.")

find_maximum()
