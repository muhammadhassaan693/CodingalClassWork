total_sum = 0

print ("This program will sum all number that you enter. To stop, enter \"0\" ")

while True:
    number = int(input("Enter a number: "))
    
    if number == 0:
        break
    
    total_sum += number

print(f"The sum of the entered numbers is: {total_sum}")