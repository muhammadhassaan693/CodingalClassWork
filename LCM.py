def HCF(small_number, larg_number):
    while (small_number):
        temp = small_number
        small_number = larg_number % small_number
        larg_number = temp

    return larg_number

first_number = int(input("Enter the small number = "))
second_number = int(input("Enter the larg number = "))

divisor = HCF(first_number, second_number)

LCM = first_number / divisor

print(f"the LCM of both number is {LCM}")