class Calculator:
    # Addition function
    def add(self, num1, num2):
        return num1 + num2
    
    # Subtraction function
    def subtract(self, num1, num2):
        return num1 - num2

    # Multiplication function
    def multiply(self, num1, num2):
        return num1 * num2
    
    # Division function with condition if the second number == 0 can not divide
    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
        

# Example usage
# Create an object
calculator = Calculator()

# Taking user input for two numbers and an operation
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Performing the operation
if operation == '+':
    result = calculator.add(x, y)
elif operation == '-':
    result = calculator.subtract(x, y)
elif operation == '*':
    result = calculator.multiply(x, y)
elif operation == '/':
    result = calculator.divide(x, y)
else:
    result = "Invalid operation"

print("The result is:", result)
