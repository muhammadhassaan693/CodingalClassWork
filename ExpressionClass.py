class Expression:
    def __init__(self, num1, num2, num3):
        """Constructor to initialize the instance attributes."""
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_sum(self):
        """Method to calculate and print the sum of the three numbers."""
        total = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {total}")

# Creating objects of the Expression class
expr1 = Expression(5, 10, 15)
expr2 = Expression(20, 30, 50)

# Calling the method to calculate and print the sum
expr1.calculate_sum()  # Output: The sum of 5, 10, and 15 is: 30
expr2.calculate_sum()  # Output: The sum of 20, 30, and 50 is: 100