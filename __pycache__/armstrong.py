number = int(input("please enter any number = "))

result = 0
temp = number

while temp > 0 :
    digit = temp % 10
    result = result + digit ** 3
    temp = temp // 10

print(f"the result is {result}")
print()

if number == result:
    print(f"{number} is an armstrong number")
else:
    print(f"{number} is not an armstrong number")