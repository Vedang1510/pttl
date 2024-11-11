# Enter the number of rows: 5
#     A 
#    B C 
#   D E F 
#  G H I J 
# K L M N O 

def alphabet_pattern_2():
    rows = int(input("Enter the number of rows: "))
    char = 65  # ASCII value of 'A'
    
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")  # Adding spaces for alignment
        for j in range(i):
            print(chr(char), end=" ")
            char += 1
        print()

alphabet_pattern_2()
