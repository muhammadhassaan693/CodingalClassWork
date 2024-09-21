number=int(input("enter any number= "))

#nested if is inside of if 
if number > 50:
    print("number greater then fifty")
    if number%2==0 :
        print("and it is even number too")
    else:
        print("it is odd number too")
else:
    print("number is less then fifty")
