# Enter the number of rows: 5
#     A 
#    B C 
#   D E F 
#  G H I J 
# K L M N O 
#  K L M N O 
#   G H I J 
#    D E F 
#     B C 
#      A 

def alphabet_pattern_4():
    rows = int(input("Enter the number of rows: "))
    char = 65  # ASCII value of 'A'
    
    # Upper half of the diamond
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(i):
            print(chr(char), end=" ")
            char += 1
        print()

    # Lower half of the diamond
    char = 65
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(i):
            print(chr(char), end=" ")
            char += 1
        print()

alphabet_pattern_4()
