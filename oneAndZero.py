def numberOfBit(num):
    ones = 0
    zeroes = 0

    while num :
        if num & 1 == 1:
            ones = ones + 1
        else:
            zeroes = zeroes + 1

        #right shift the binary code
        num = num >> 1

    print(f"number of ones is = {ones} ")
    print(f"number of zeroes is = {zeroes} ")

number = int(input("Enter any number = "))
numberOfBit(number)