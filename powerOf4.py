def powerOf4(number):
    count = 0

    # checking if only one set bit exists
    if (number & (~(number & (number - 1)))):
        while number > 1: # count 0 bit befor set bit
            number = number >> 1
            count = count + 1

        if count % 2 == 0 :
            return True
        else:
            return False
        
num = int(input("Enter any number = "))
result = powerOf4(num)

if result == True:
    print("The number is a power of 4")
else:
    print("The number is not a power of 4 ")