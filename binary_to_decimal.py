#function to convert from binary to decimal
def binary_to_decimal(binary):
    decimal = 0
    i = 0

    while binary != 0:
        temp = binary % 10
        decimal = decimal + temp * pow(2,i)
        binary = binary // 10

        i = i + 1

    return decimal

# Get binary input from the user
binary_input = int(input("Enter your binary number = "))

decimal_output = binary_to_decimal(binary_input)

# Print the decimal output
print("Decimal:", decimal_output)