def multiply_one_iteration(a, b):
    return a * b

def multiply_n_iterations(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result

# Take input from the user
a = int(input("Enter 'a' for a*b: "))
b = int(input("Enter 'b' for a*b: "))

# Calculate and print results
print(multiply_one_iteration(a, b))
print(multiply_n_iterations(a, b))