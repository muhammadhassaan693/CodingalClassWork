#first approach
def multiplication_v1(f_num, s_num):
    result = f_num * s_num
    print(f"the multiplication result is {result}")
    print("the process is done with 1 itaration")

#second approach
def multiplication_v2(f_num, s_num):
    result = 0
    for i in range(1, s_num + 1):
        result = result + f_num
        print(f"result of addition of the first number = {result}")

    print(f"the process is done with {s_num} itaration")

fnum=int(input("please enter the first number = "))
snum=int(input("please enter the second number = "))

multiplication_v1(fnum, snum)
print()

multiplication_v2(fnum, snum)
