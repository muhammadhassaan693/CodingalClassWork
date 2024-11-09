#first approach
def f_approach(number):
    print("iteration for first approach is only 1x")
    return number*(number+1)/2

print(f_approach(5)) 
print()

#second approach
def s_approach(number):
    sum=0
    for i in range(1, number+1):
        sum = sum + i

    print(f"iteration for second approach is {i}x")
    return sum

print(s_approach(5))
print()