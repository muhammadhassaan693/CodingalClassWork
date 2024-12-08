def powerOf2(number):
    if number <= 0:
        return False
    else:
        if (number & (number - 1)) == 0:
            return True
        else:
            return False
        
num = int(input("Enter any number = "))
result = powerOf2(num)

if result == True:
    print("The number is a power of 2 ")
else:
    print("The number is not a power of 2 ")