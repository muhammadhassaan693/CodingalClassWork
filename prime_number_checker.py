from math import sqrt

number = int(input("Enter any number to be check = "))

if number > 1:
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            print("This is not a prime number ")
            break
    else:
        print("This number is a prime number")

else:
    print("this number is not a prime number ")