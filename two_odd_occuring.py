def twoOdd(array1, size):
    xor_of_2 = array1[0]

    x= 0
    y= 0
    set_bit = 0

    for i in range(1, size) :
        xor_of_2 = xor_of_2 ^ array1[i]

    set_bit = xor_of_2 & ~(xor_of_2 - 1)

    for i in range(size):
        if array1[i] & set_bit :
            x = x ^ array1[i]
        else:
            y = y ^ array1[i]

    print(f"two odd occuring elements are {x} and {y}")