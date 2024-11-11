def check_armstrong():
    # Taking input from the user
    num = int(input("Enter a number to check if it is an Armstrong number: "))
    
    # Converting the number to string to find the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculating the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Checking if the sum of powers equals the original number
    if sum_of_powers == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

check_armstrong()
