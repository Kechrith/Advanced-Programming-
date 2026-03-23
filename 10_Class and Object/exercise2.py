# Write a program to Calculator Program using OOP (Class and Object)
# Define a class named Calculator
class Calculator:
    
    # Constructor: initialize object with num1, operator, num2
    def __init__(self, num1, operator, num2):
        self.num1 = num1        # first number
        self.operator = operator  # operator (+, -, *, /, ^, %)
        self.num2 = num2        # second number

    # Method for addition
    def add(self):
        return self.num1 + self.num2

    # Method for subtraction
    def subtract(self):
        return self.num1 - self.num2

    # Method for multiplication
    def multiply(self):
        return self.num1 * self.num2

    # Method for division
    def divide(self):
        if self.num2 == 0:
            return "Error: Cannot divide by zero"
        return self.num1 / self.num2

    # Method for power
    def power(self):
        return self.num1 ** self.num2

    # Method for modulo
    def modulo(self):
        return self.num1 % self.num2

    # Method to choose operation based on operator
    def calculate(self):
        if self.operator == '+':
            return self.add()
        elif self.operator == '-':
            return self.subtract()
        elif self.operator == '*':
            return self.multiply()
        elif self.operator == '/':
            return self.divide()
        elif self.operator == '^':
            return self.power()
        elif self.operator == '%':
            return self.modulo()
        else:
            return "Invalid operator"


# =========================
# TEST PROGRAM (MAIN PART)
# =========================

# Ask user to input values
user_input = input("Enter number1, operator and number2 (e.g., 5 + 3): ")

# Split input into parts
parts = user_input.split()

# Convert input values
num1 = float(parts[0])
operator = parts[1]
num2 = float(parts[2])

# Create Calculator object
calc = Calculator(num1, operator, num2)

# Call calculate method
result = calc.calculate()

# Display result
print(num1, operator, num2, "=", result)