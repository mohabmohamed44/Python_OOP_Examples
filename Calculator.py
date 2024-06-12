# Class Calculator to preform basic arithmetic Operations (addition) (subtraction) (multiplication) (division)
class Calculator:
    # Addition function
    def add(self,num1,num2):
        return num1 + num2
    
    # subtraction function
    def subtract(num1,num2):
        return num1 - num2
    # multiplication function
    def multiply(num1, num2):
        return num1 * num2
    
    # Division function with condition if the second number == 0 can not divide
    def divide(num1,num2):
        if num2 != 0:
            return num1 / num2
        else:
            return ("Cannot divide by zero")
        

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
