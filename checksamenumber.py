def check_if_same_number(n1, n2):
    if (n1 ^ n2) == 0 :
        print("both numbers are equal")
    else:
        print("both numbers are not equal")

first_number = int(input("enter the first number = "))
second_number = int(input("enter the second number = "))

check_if_same_number(first_number, second_number)
