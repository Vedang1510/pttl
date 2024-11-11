def check_palindrome():
    # Taking input from the user
    value = input("Enter a string or number to check if it is a palindrome: ")
    
    # Removing spaces and converting to lowercase for consistent checking
    cleaned_value = value.replace(" ", "").lower()
    
    # Checking if the cleaned value is the same forward and backward
    if cleaned_value == cleaned_value[::-1]:
        print(f"'{value}' is a palindrome.")
    else:
        print(f"'{value}' is not a palindrome.")

check_palindrome()
