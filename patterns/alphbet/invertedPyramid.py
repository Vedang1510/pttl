def alphabet_pattern_3():
    rows = int(input("Enter the number of rows: "))
    char = 65  # ASCII value of 'A'
    
    for i in range(rows, 0, -1):
        print(" " * (rows - i), end="")  # Adding spaces for alignment
        for j in range(i):
            print(chr(char), end=" ")
            char += 1
        print()

alphabet_pattern_3()

# Enter the number of rows: 5
# K L M N O 
#  G H I J 
#   D E F 
#    B C 
#     A 
