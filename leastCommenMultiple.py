# Function to calculate LCM
def calculate_lcm(x, y):
    # Calculate the greater number
    greater = max(x, y)
    
    # Loop until we find the LCM
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

# Input from the user
largest_number = int(input("Enter Largest number: "))
smallest_number = int(input("Enter Smallest number: "))

# Calculate LCM
lcm = calculate_lcm(smallest_number, largest_number)

# Print the result
print(f"lcm is {lcm} ")