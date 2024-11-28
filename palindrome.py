number = int(input("please enter any number = "))

#Temporary variable for helper
temp = number
reverse = 0

#reversing number until the last digit
while number > 0:
    remainder = number%10
    reverse = reverse * 10 + remainder
    number = number //10

print(f"the reversed number is {reverse}")
print()

if temp == reverse:
    print(f"{temp} is a palindrome")

else:
    print(f"{temp} is not a palindrome")