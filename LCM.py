<<<<<<< HEAD
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

=======
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

>>>>>>> d20d01aef834badc6cdd3b55c8a6a43f97416d0d
print(f"the LCM of both number is {LCM}")