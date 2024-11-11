def check_number():
    # Taking input from the user
    num = float(input("Enter a number to check if it is positive, negative, or zero: "))
    
    # Checking if the number is positive, negative, or zero
    if num > 0:
        print(f"{num} is a positive number.")
    elif num < 0:
        print(f"{num} is a negative number.")
    else:
        print(f"{num} is zero.")

check_number()
    