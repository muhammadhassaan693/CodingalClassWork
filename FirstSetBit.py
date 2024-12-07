def rightmost_set_bit_position(n):
    if n == 0:
        return -1  # No set bits in 0
    position = 1
    while n > 0:
        if n & 1:  # Check if the least significant bit is set
            return position
        n >>= 1  # Right shift to check the next bit
        position += 1

# Take input from the user
number = int(input("Enter number: "))
position = rightmost_set_bit_position(number)

if position == -1:
    print("No set bits found.")
else:
    print(f"Position of the first set bit: {position}")