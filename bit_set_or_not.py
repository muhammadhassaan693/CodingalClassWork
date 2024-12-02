def SetOrNot(num,position):
    if (position & 1) == 1 or (position & 1) == 0 :
        if num & (1 << (position - 1)):
            print("this is set bit")
        else:
            print("this is not set bit")

number = int(input("Enter the number = "))
pos = int(input("Enter the bit position to be checked = "))
print()

SetOrNot(number, pos)