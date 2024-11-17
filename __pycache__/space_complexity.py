def sum_number(number):
    return number * (number + 1)/2

def sum_list(array):
    sum = 0
    for i in array:
        sum = sum + i

    return sum

n = 9
array_number = [5, 3, 1, 8]

print(f"the total sum of the first {n} number is {sum_number(n)} ")
print()

print(f"the total sum of the array element is {sum_list(array_number)}")