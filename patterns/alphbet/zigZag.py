# Enter the number of rows: 3
# A B C D E F G 
# H I J K L M N 
# O P Q R S T U 

def alphabet_pattern_5():
    rows = int(input("Enter the number of rows: "))
    char = 65  # ASCII value of 'A'
    
    for i in range(1, rows + 1):
        for j in range(1, rows + 1):
            print(chr(char), end=" ")
            char += 1
            if char > 90:  # If 'Z' is reached, reset to 'A'
                char = 65
        print()

alphabet_pattern_5()
